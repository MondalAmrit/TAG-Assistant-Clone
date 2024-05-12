###############################################
# 1. Get the tokenizer and add the slot tokens
# 2. Define the data in synthetic manner. (Single slot only)
# 3. Get tokens length of prefix, slot data and suffix.
# 4. Now the target tokens will be,
"""
prefix_tokens = tokenizer.encode(prefix)
suffix_tokens = tokenizer.encode(suffix)
slot_tokens = len( tokenizer.encode(slot_data) )
inp = prefix_tokens + slot_tokens + suffix_tokens
slot_tokens = [ tokenizer.id_to_tkn('[B-slot]') ] + [ tokenizer.id_to_tkn('[I-slot]) ] * max( 0,len(slot_tokens)-1 )

tgt = [ 0 ] * len( prefix_tokens ) + slot_tokens + [ 0 ] * len( suffix_tokens )
dataset.append( [inp,tgt] )
"""
# 5. In this way slot filling dataset can be generated.

import random, pprint, csv
from transformers import BertTokenizerFast

# Define Slot token Names
slot_tokens = {
    "Location" : ['B-Location','I-Location'],
    "Query" : ['B-Query','I-Query'],
    "Quantity" : ['B-Qty','I-Qty'],
    "Datetime": ['B-Datetime','I-Datetime'],
}

# Load the tokenizer (BERT)
# Add Some Special tokens
special_tokens = ['[QUES]']
for v in slot_tokens.values():
    special_tokens.extend(v)
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
if len(special_tokens) > 0:
    tokenizer.add_special_tokens({'additional_special_tokens': special_tokens})
vocab_size = tokenizer.vocab_size + len(special_tokens)
print('Vocab Size is:', vocab_size)

# Define the dataset conversion
def create_examples(data, slot_type, split = 0.9):
    global tokenizer, slot_tokens
    """ data[0] : Prefix   data[1] : Slot data (Cannot be empty)    data[2] : Suffix """
    dataset = []
    for d in data:
        pref = tokenizer.encode(d[0], add_special_tokens = False) if d[0] != '' else []
        suff = tokenizer.encode(d[2], add_special_tokens = False) if d[2] != '' else []
        slot = tokenizer.encode(d[1], add_special_tokens = False)
        # Remember to add [CLS] : 101  and [SEP] : 102
        inp = [101] + pref + slot + suff + [102]
        B_slot, I_slot = slot_tokens[slot_type]
        slot = tokenizer.encode(B_slot, add_special_tokens = False) + tokenizer.encode(I_slot, add_special_tokens = False) * max(0,len(slot)-1)
        tgt = [0]*(len(pref) + 1) + slot + [0]*(len(suff) + 1) # 1 is for [CLS] and [SEP]
        dataset.append([inp,tgt])
    random.shuffle(dataset)
    split_idx = int(len(dataset)*split)
    return dataset[:split_idx], dataset[split_idx:]

def combine_data(prefixes, slots, suffixes, slot_type, split = 0.9):
    data = []
    for p in prefixes:
        for slot in slots:
            for s in suffixes:
                data.append([p,slot,s])
    return create_examples(data, slot_type, split)

# Define Synthetic Data
def generate_synthetic_data(split = 0.9):
    train_dataset, test_dataset = [], []
    # Qty Examples
    prefixes = ['set the volume to ', 'set the brightness to ', "Why don't you make the volume to ",
                "Why don't you make the brightness to ", "Increase the volume by ", "Decrease the volume by ",
                "Increase the volume by ", "Decrease the volume by "]
    # slots = list(range(101))
    slots = ['10','15','12','23','45','74']
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Quantity', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])

    # Search Query
    prefixes = ['Search for ', 'Youtube search for ', 'Search related articles for ',
                'generate images for ','Search for images related to ', 'I want images of the ',
                'search for related video ']
    slots = ['Ai','Python','Java','home tutorials','how to play chess','how earn money faster',
             "DIY tips and tricks",'how to foucs on study?','cooking']
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Query', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])
    prefixes = ['I want you to search for ', 'search for related videos of ', ]
    suffixes = ['on internet', 'on Youtube', 'on Google',]
    res = combine_data(prefixes, slots, suffixes, 'Query', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])

    # Music Search Queries
    prefixes = ['Play the song of ', 'search for a song ', 'Play a song from ',
                'I want you to play a song of ']
    slots = ['Alan Walker','Justin Biber', 'A R Rahman','Arijit Singh', 'Sonu Nigam']
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Query', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])

    return train_dataset, test_dataset
    
train_data, test_data = generate_synthetic_data(split=0.9)

print('Total Examples: ', len(train_data) + len(test_data))
print('Training Examples:')
pprint.pprint(train_data[:5])
print('Testing Examples:')
pprint.pprint(test_data[:5])

print('\n\nExample of this conversion:')
print([tokenizer.decode(train_data[0][0]), tokenizer.decode(train_data[0][1])])

print('\nWriting to csv files')
for i in ('train','val'):
    with open(f'C://users/Anirudh/Desktop/TAG_slot_filling_v0_{i}.csv','w', newline='') as f:
        writer = csv.writer(f)
        if i == 'train':
            writer.writerows(train_data)
        else:
            writer.writerows(test_data)