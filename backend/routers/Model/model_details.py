import torch, math
from torch import nn
import torch.nn.functional as F

from .pre_processing import config, tokenizer

class CausalSelfAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        assert config.d_model % config.num_heads == 0
        # key, query, value projections for all heads, but in a batch
#         self.c_attn = nn.Linear(config.d_model, 3 * config.d_model, bias=config.bias)
        self.expt_layer_a, self.expt_layer_b, self.expt_layer_c = nn.ModuleList([nn.Linear(config.d_model,config.d_model) for _ in range(3)])
        # output projection
        self.c_proj = nn.Linear(config.d_model, config.d_model, bias=config.bias)
        # regularization
        self.attn_dropout, self.resid_dropout = nn.Dropout(config.dropout), nn.Dropout(config.dropout)
        self.num_heads, self.d_model, self.dropout = config.num_heads, config.d_model, config.dropout
        # flash attention make GPU go brrrrr but support is only in PyTorch >= 2.0
        self.flash = hasattr(torch.nn.functional, 'scaled_dot_product_attention')
        if not self.flash:
            print("WARNING: using slow attention. Flash Attention requires PyTorch >= 2.0")
            # causal mask to ensure that attention is only applied to the left in the input sequence
            self.register_buffer("bias", torch.tril(torch.ones(config.seq_len, config.seq_len))
                                        .view(1, 1, config.seq_len, config.seq_len))

    def forward(self, x):
        B, T, C = x.size() # batch size, sequence length, embedding dimensionality (d_model)

        # calculate query, key, values for all heads in batch and move head forward to be the batch dim
#         q, k, v  = self.c_attn(x).split(self.d_model, dim=2)
        q,k,v = self.expt_layer_a(x), self.expt_layer_b(x), self.expt_layer_c(x)
        q,k,v = [i.view(B, T, self.num_heads, C // self.num_heads).transpose(1, 2) for i in (q,k,v)] # (B, nh, T, hs)
        # causal self-attention; Self-attend: (B, nh, T, hs) x (B, nh, hs, T) -> (B, nh, T, T)
        if self.flash:
            # efficient attention using Flash Attention CUDA kernels
            y = torch.nn.functional.scaled_dot_product_attention(q, k, v, attn_mask=None, dropout_p=self.dropout if self.training else 0, is_causal=True)
        else:
            # manual implementation of attention
            att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
            att = att.masked_fill(self.bias[:,:,:T,:T] == 0, float('-inf'))
            att = self.attn_dropout(F.softmax(att, dim=-1))
            y = att @ v # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
        y = y.transpose(1, 2).contiguous().view(B, T, C) # re-assemble all head outputs side by side
        # output projection
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
    self.csa = CausalSelfAttention(config)
    self.ff = MLP(config)
    self.ln1, self.ln2 = [LayerNorm(config.d_model,config.bias) for _ in range(2)]
  def forward(self, x):
    x += self.csa(self.ln1(x.clone()))
    return x + self.ff(self.ln2(x.clone()))

class GPT(nn.Module):
  def __init__(self, config):
    super().__init__()
    self.token_embedding_table = nn.Embedding(config.vocab_size, config.d_model, padding_idx = 0)
    self.postion_embedding_table = nn.Embedding(config.seq_len, config.d_model, padding_idx = 0)
    self.blocks = nn.ModuleList([Block(config) for _ in range(config.num_layers)])
    self.ln = LayerNorm(config.d_model,config.bias)
    self.out_proj = nn.Linear(config.d_model,config.vocab_size, bias = config.bias)
    self.seq_len, self.drop = config.seq_len, nn.Dropout(config.dropout)
  def forward(self, x, targets = None):
    # x : (Batch_Size, Seq_len)    # targets : (Batch_Size, Seq_len)
    B, S = x.shape
    x = self.drop(self.token_embedding_table(x) + self.postion_embedding_table(torch.arange(0, S, device = x.device)))
    for module in self.blocks:   x = module(x)
    logits, loss = self.out_proj(self.ln(x)), None
    if targets != None:
      B, S, V = logits.shape
      loss = F.cross_entropy(logits.view(B*S, V), targets.view(B*S).long(), ignore_index = 0)
    return logits, loss

  @property
  def device(self):   return next(self.parameters()).device

  @torch.no_grad()
  def generate(self, prompt, num_tokens = 100):
    global tokenizer
    self.eval()
    self.to(device = config.device)
    
    inp = tokenizer.encode(f'<START> {prompt} <END>'.lower())[-self.seq_len:]
    inp = torch.tensor( inp, dtype = torch.int ).to(device = self.device)

    for _ in range(num_tokens):
        logits, _ = self(inp[-self.seq_len:].unsqueeze(dim=0))
        tkn = torch.multinomial( F.softmax(logits[:,-1,:], dim = -1), num_samples = 1 ).to(device = self.device)
        inp = torch.cat( (inp, tkn[0]), dim=-1 )
        
    m = tokenizer.decode(inp)
    s,e = m.find('< text >') + len('< text >'), m.find('< / text >')
    print("MultiNomial:",m[s:e])
    return m[s:e]
  
print('Loaded the model class')