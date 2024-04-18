import torch
from routers.Model.model_details import CausalSelfAttention, MLP, LayerNorm, Block, GPT
from routers.Model.pre_processing import config
import __main__

setattr(__main__,'CausalSelfAttention',CausalSelfAttention)
setattr(__main__,'MLP',MLP)
setattr(__main__,'LayerNorm',LayerNorm)
setattr(__main__,'Block',Block)
setattr(__main__,'GPT',GPT)
print('Downloading the model...')
model = torch.load('./routers/Model/pre_train_TAG_v1.pkt',map_location='cpu')
model.eval()