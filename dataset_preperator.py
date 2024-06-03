import random, os
from transformers import BertTokenizerFast
# os.chdir('C://Users/Anirudh/Desktop/Startup/TAG-Assistant-Clone')
print(os.listdir())

from backend.Intents.Call.examples import generate_dataset as call_examples
from backend.Intents.Camera.examples import generate_dataset as camera_examples
from backend.Intents.Chat.examples import generate_dataset as chat_examples
from backend.Intents.Email.examples import generate_dataset as email_examples
from backend.Intents.FileConverter.examples import generate_dataset as file_converter_examples
# from backend.Intents.GIT.examples import generate_dataset as git_examples
from backend.Intents.Internet.examples import generate_dataset as internet_examples
from backend.Intents.Music.examples import generate_dataset as music_examples
from backend.Intents.News.examples import generate_dataset as news_examples
from backend.Intents.Notes.examples import generate_dataset as notes_examples
from backend.Intents.Tools.examples import generate_dataset as tools_examples
from backend.Intents.System.examples import generate_dataset as system_examples
from backend.Intents.Weather.examples import generate_dataset as weather_examples
from backend.Intents.YouTube.examples import generate_dataset as youtube_examples

import pprint, csv


# Get the datasets for the slot filling
data_list = [ weather_examples(), notes_examples(), call_examples(), camera_examples(),
             internet_examples(), music_examples(), youtube_examples(), system_examples(),
             email_examples(), file_converter_examples(), news_examples(), tools_examples()]

# Define the Slot labels
slot_labels = {
    "Basic" : ["O","[UNK]"],
    "Location" : ["B-LOC","I-LOC"],
    "Quantity" : ["B-QTY","I-QTY"],
    "Query" : ["B-QUERY","I-QUERY"],
    "Date" : ["B-DATE","I-DATE"],
    "Time" : ["B-TIME","I-TIME"],
}

# Define the tokenizer
special_tokens = ['[QUES]']
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
if len(special_tokens) > 0:
    tokenizer.add_special_tokens({'additional_special_tokens': special_tokens})
print("The vocab size of tokenizer is: ",tokenizer.vocab_size + len(special_tokens))


print("\n\nPreforming a Sample check:")
sample = "This is a sample? {check_this}"
print("Sample: ",sample)
print("Tokens: ", tokenizer.tokenize(sample))

# Perform the Slot Filling
def slot_filling_data(sentence, intentClass, slot_tokens):
        global tokenizer, slot_labels
        res = []
        # Tokenize the entire sentence
        tokens = tokenizer.tokenize(sentence)
        
        # Annotate slot tokens
        in_slot = False
        tkn = ''
        for token in tokens:
            if token[0] == '{':
                in_slot = True
                if tkn != '': # This means { is in example itself
                     tkn = tkn.replace("#","")
                     res.extend(['O' for i in range(len(tokenizer.tokenize(tkn)))])
                tkn = token
            elif token[0] == '}':
                 in_slot = False
                 tkn += token
                 tkn = tkn[1:-1].replace("#","").capitalize() # Excluding curly brackets
                 # Split by _ coz Location_1 like things may occur
                 slot_tkn = slot_labels.get(tkn.split('_')[0],'Basic') # Get the corresponding slot tokens to be replaced
                 s = tokenizer.tokenize(slot_tokens.get(tkn,'')) # Get the token count
                 res.extend([slot_tkn[0]] + [slot_tkn[1]]*max(0,len(s)-1))
            elif in_slot:
                 tkn += token
            else:
                 res.append('O')
        
        try:
            for k,v in slot_tokens.items():
                sentence = sentence.replace("{"+k+"}",v)
        except:
             print(slot_tokens)
             raise 'Error occured here'
        return [sentence, intentClass, " ".join(res)]

dataset = {'train':[],'val':[]}
count = 0
for i in data_list:
    print(count)
    count += 1
    for j in ('train','val'):
        ds = []
        for k in i[0 if j=='train' else 1]:
              ds.append(slot_filling_data(*k))
        dataset[j].extend(ds.copy())
        ds.clear()

random.shuffle( dataset['train'] )
random.shuffle( dataset['val'] )

print(f"Training Dataset: {len(dataset['train']):,}\tValidation Dataset: {len(dataset['val']):,}\n")
print("\nFirst Four examples:")
pprint.pprint(dataset['train'][:4])
pprint.pprint(dataset['val'][:4])

# Add the chat data to the final resultant dataset
res = chat_examples()
dataset['train'].extend(res[0])
dataset['val'].extend(res[1])

print("\nLast Two examples:")
pprint.pprint(dataset['train'][-2:])
pprint.pprint(dataset['val'][-2:])

for i in ('train','val'):
    with open(f'C://users/Anirudh/Desktop/TAG_dataset_{i}.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dataset[i])

print('Dataset uploaded')