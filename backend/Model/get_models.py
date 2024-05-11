import torch

# Get the GPT model
from Model.GPT_Model.model_details import GPT
from Model.GPT_Model.pre_processing import config

# Get the BERT Classification model
from Model.BERT_Classification_Model.model_details import BERTForClassification
from Model.BERT_Classification_Model.pre_processing import config as bert_config

print('Downloading the GPT model...')
GPTmodel = GPT(config)
GPTmodel.load_state_dict( torch.load('./Model/state_dicts/fine_tuned_TAG_v_0_state_dict.pt',map_location='cpu') )
GPTmodel.eval()
print('Downloading the BERT model...')
BERTmodel = BERTForClassification(bert_config)
BERTmodel.load_state_dict( torch.load('./Model/state_dicts/BERT_Classification_state_dict.pt',map_location='cpu') )
BERTmodel.eval()
print('Models are online ')