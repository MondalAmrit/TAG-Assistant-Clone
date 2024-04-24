import torch
from Model.model_details import GPT
from Model.pre_processing import config

print('Downloading the model...')
model = GPT(config)
model.load_state_dict( torch.load('./Model/fine_tuned_TAG_v_0_state_dict.pt',map_location='cpu') )
model.eval()
print('Model is online now')