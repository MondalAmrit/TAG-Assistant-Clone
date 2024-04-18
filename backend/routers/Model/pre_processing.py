from dataclasses import dataclass
from transformers import BertTokenizerFast

@dataclass
class Hyperparameters:
    d_model: int = 256 #384  # Improvment benefits the accuracy
    num_heads: int = 8 #6
    dropout: float = 0.1
    seq_len: int = 50 #256  # Improving seq len is decreasing the model's capability to memorize
    bias: bool = True
    vocab_size: int = 15000
    device: str = 'cpu'
    num_layers: int = 6 #8  # Improvment benefits the accuracy
    lr: float = 1e-3
    batch_size: int = 64 #256 #128  # Doubtful
    gradient_acc_steps: int = 0
    split: float = 0.95
    tokenizer: str = 'bert'
        
    epochs: int = 1
    eval_iters: int = 200 # How many evaluation iterations to take on each training and validation
    eval_frequency: int = 2_000  # How frequent the readings are taken
    num_steps: int = 40_000    # How many steps to train.
    generate_frequency: int = 5_00 # How frequently the model generation is to be done.
    warmup_iters: int = 2000
    lr_decay_iters: int = 600_000
    min_lr: float = 1e-4
    decay_lr: bool = True
# Create an instance of the Hyperparameters data class with the provided values
config = Hyperparameters()

class BertTokenizer:
   def __init__(self, special_tokens = None):
       # Load pre-trained model tokenizer (vocabulary)
       self.tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
       if special_tokens:
            self.tokenizer.add_special_tokens({"additional_special_tokens":special_tokens})
       self.vocab_size = self.tokenizer.vocab_size + (len(special_tokens) if special_tokens else 0)

   def encode(self,text):
       return self.tokenizer.encode(text, add_special_tokens=False)

   def decode(self,lst):
       return self.tokenizer.decode(lst)

   def multi_text_decode(self,lsts):
       return self.tokenizer.batch_decode(lsts)

   def multi_text_encode(self,texts):
       return [self.tokenizer.encode(text) for text in texts]

   def token_of(self, word):
       return self.tokenizer.convert_tokens_to_ids(word)

   def value_of(self, token):
       return self.tokenizer.convert_ids_to_tokens(token)
   
tokenizer = BertTokenizer()
config.vocab_size = tokenizer.vocab_size

