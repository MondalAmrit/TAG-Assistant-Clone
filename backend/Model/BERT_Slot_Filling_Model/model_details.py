import torch, math
from torch import nn
import torch.nn.functional as F

from .pre_processing import config, tokenizer
    

# Define Slot token Names
slot_tokens = {
    "Location" : ['B-Location','I-Location'],
    "Query" : ['B-Query','I-Query'],
    "Quantity" : ['B-Qty','I-Qty'],
    "Datetime": ['B-Datetime','I-Datetime'],
}
slot_token_lst = ['[PAD]','[UNK]']
for v in slot_tokens.values():
    slot_token_lst.extend(v)
    
def slot_decode( lst ):
    return ' '.join([slot_token_lst[idx] if idx < len(slot_token_lst) and idx > 0 else '[UNK]' for idx in lst])

def extract_slot( pred, dec ):
    assert len(pred) == len(dec)
    res = []
    for i in range(len(dec)):
        # Single slot assumed
        if dec[i] < len(slot_token_lst) and dec[i] > 1 and pred[i] != 0:
            res.append(pred[i])
    return res


class SelfAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        assert config.d_model % config.num_heads == 0
        # key, query, value projections for all heads, but in a batch
        self.c_attn = nn.Linear(config.d_model, 3 * config.d_model, bias=config.bias)
        self.c_proj = nn.Linear(config.d_model, config.d_model, bias=config.bias)
        
        self.attn_dropout, self.resid_dropout = nn.Dropout(config.dropout), nn.Dropout(config.dropout)
        self.num_heads, self.d_model, self.dropout = config.num_heads, config.d_model, config.dropout

    def forward(self, x, attn_mask):
        B, T, C = x.size() # batch size, sequence length, embedding dimensionality (d_model)
        q,k,v = self.c_attn(x).split(self.d_model, dim=2)
        q,k,v = [i.view(B, T, self.num_heads, C // self.num_heads).transpose(1, 2) for i in (q,k,v)] # (B, nh, T, hs)
        # self-attention; Self-attend: (B, nh, T, hs) x (B, nh, hs, T) -> (B, nh, T, T)

        # manual implementation of attention
        att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
        attn = attn_mask.unsqueeze(1).repeat(1,self.num_heads,1).unsqueeze(-1)
        att = att.masked_fill(attn, -1e9)
        att = self.attn_dropout(F.softmax(att, dim=-1))
        y = att @ v # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
        y = y.transpose(1, 2).contiguous().view(B, T, C) # re-assemble all head outputs side by side
        return self.resid_dropout(self.c_proj(y))

class MLP(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.c_fc    = nn.Linear(config.d_model, 4 * config.d_model, bias=config.bias)
        self.gelu    = nn.GELU()
        self.c_proj  = nn.Linear(4 * config.d_model, config.d_model, bias=config.bias)
        self.dropout = nn.Dropout(config.dropout)

    def forward(self, x):
        x = self.gelu(self.c_fc(x))
        return self.dropout(self.c_proj(x))

class LayerNorm(nn.Module):
    """ LayerNorm but with an optional bias. PyTorch doesn't support simply bias=False """
    def __init__(self, ndim, bias):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(ndim))
        self.bias = nn.Parameter(torch.zeros(ndim)) if bias else None

    def forward(self, input):
        return F.layer_norm(input, self.weight.shape, self.weight, self.bias, 1e-5)
    

class Block(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.sa = SelfAttention(config)
        self.ff = MLP(config)
        self.ln1, self.ln2 = [LayerNorm(config.d_model,config.bias) for _ in range(2)]
    def forward(self, x, attn_mask):
        x += self.sa( self.ln1(x.clone()), attn_mask )
        return x + self.ff( self.ln2(x.clone()) )

class BERT(nn.Module):
    """ The base BERT class that is used as a core for any down streamed task """
    def __init__(self, config):
        super().__init__()
        self.tok_embed = nn.Embedding(config.vocab_size, config.d_model)  # token embedding
        self.pos_embed = nn.Embedding(config.seq_len, config.d_model)  # position embedding
        self.blocks = nn.ModuleList([Block(config) for _ in range(config.num_layers)])
        self.seq_len, self.drop = config.seq_len, nn.Dropout(config.dropout)
    def forward(self, x, attn_mask = None):
        # x : (Batch_Size, Seq_len)    # targets : (Batch_Size, Seq_len)
        S = x.shape[-1]
        x = self.drop(self.tok_embed(x) + self.pos_embed(torch.arange(0, S, device = x.device)))
        for module in self.blocks:   x = module(x, attn_mask)
        return x
    @property
    def device(self):   return next(self.parameters()).device
    
class BERTForSlotFilling(nn.Module):
    """ Down streamed for the Slot Filling task. Mostly done in Fine Tuning """
    def __init__(self, config):
        super().__init__()
        self.bert = BERT(config)
        self.drop = nn.Dropout(config.dropout)
        self.out_proj = nn.Linear(config.d_model,config.num_slots)
        self.seq_len = config.seq_len
    def forward(self, x, attn_mask = None, tgt = None):
        # No dropout layer is being considered here
        if attn_mask == None:     attn_mask = (x == 0)  # Attention mask is created based on [PAD] tokens
        logits = self.out_proj( self.drop(self.bert( x, attn_mask )) )
        if tgt != None:
            V = logits.shape[-1]
            loss = F.cross_entropy( logits.view(-1,V),tgt.view(-1).long(),ignore_index=0 )
            return logits, loss
        return logits
    
    @property
    def device(self):   return next(self.parameters()).device
    
    @torch.no_grad()
    def predict(self, x):  # x : (Seq Len)
        global tokenizer
        seq = tokenizer.encode(x)
        if len(seq) < self.seq_len:     seq += [0]*max(0,self.seq_len-len(seq))
        x= torch.tensor( seq, device = self.device )
        out = self(x[-self.seq_len:].unsqueeze(0)).argmax(-1)[0]     # Input : (1,seq_len)  Output : (1,) seq_len = 0 index
        slot_values = extract_slot(x[-self.seq_len:].tolist(), out.tolist())
        return tokenizer.decode(slot_values) if len(slot_values) > 0 else ''