import torch, os, sys

# Add the directory containing shared Python files to the module search path
shared_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Model'))
print("Shared Dir: ", shared_dir)
# sys.path.append(shared_dir)
# Get the GPT model
from GPT_Model.model_details import GPT
from GPT_Model.pre_processing import config

# Get the BERT Classification model
from BERT_Classification_Model.model_details import BERTForClassification
from BERT_Classification_Model.pre_processing import config as bert_config

# Get the BERT Slot Filling model
from BERT_Slot_Filling_Model.model_details import BERTForSlotFilling
from BERT_Slot_Filling_Model.pre_processing import config as bert_slot_config

def get_gpt():
    print('Downloading the GPT model...')
    GPTmodel = GPT(config)
    GPTmodel.load_state_dict( torch.load(shared_dir + '/state_dicts/fine_tuned_TAG_v_1_state_dict.pt',map_location='cpu') )
    GPTmodel.eval()
    return GPTmodel

def get_bert_classification():
    print('Downloading the BERT model...')
    BERTmodel = BERTForClassification(bert_config)
    BERTmodel.load_state_dict( torch.load(shared_dir + '/state_dicts/BERT_Classification_state_dict_v0.pt',map_location='cpu') )
    BERTmodel.eval()
    return BERTmodel

def get_bert_slot_filling():
    print('Downloading the slot filling model...')
    BERTSlotFilling = BERTForSlotFilling(bert_slot_config)
    BERTSlotFilling.load_state_dict( torch.load(shared_dir + '/state_dicts/BERT_Slot_filling_state_dict_v0.pt',map_location='cpu') )
    BERTSlotFilling.eval()
    return BERTSlotFilling