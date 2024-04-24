from dataclasses import dataclass
from transformers import BertTokenizerFast
##############################################
# Hyper parameters
@dataclass
class Hyperparameters:
    # Main Structure deciding params
    d_model: int = 256
    num_heads: int = 8
    num_layers: int = 8
    
    # Secondary structure deciding params
    dropout: float = 0.1
    seq_len: int = 128
    vocab_size: int = 15000
    batch_size: int = 128
    gradient_acc_steps: int = 0
    bias: bool = True
    
    # Data set control params
    split: float = 0.95
    device: str = 'cpu'
    
    # Training params
    epochs: int = 1       # How many times training needs to be repeated
    eval_iters: int = 200 # How many evaluation iterations to take on each training and validation
    eval_frequency: int = 5_00  # How frequent the readings are taken
    num_steps: int = 8_000    # How many steps to train.
    generate_frequency: int = 2_000 # How frequently the model generation is to be done.
    loss_buffer: int = 0.5 # Early Stopping (How much loss increase is tolerated)
    
    # Optimizer params
    lr: float = 1e-3
    warmup_iters: int = 2000
    lr_decay_iters: int = 600_000   
    min_lr: float = 1e-4
    decay_lr: bool = True
        
# Create an instance of the Hyperparameters data class with the provided values
config = Hyperparameters()

###################################################
# Tokenizer
special_tokens = ['[QUES]']
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
if len(special_tokens) > 0:
    tokenizer.add_special_tokens({'additional_special_tokens': special_tokens})
config.vocab_size = tokenizer.vocab_size + len(special_tokens)

