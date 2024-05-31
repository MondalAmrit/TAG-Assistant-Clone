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
special_tokens = ['[QUES]']
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
if len(special_tokens) > 0:
    tokenizer.add_special_tokens({'additional_special_tokens': special_tokens})
vocab_size = tokenizer.vocab_size + len(special_tokens)

# Slot tokens
slot_token_lst = ['[PAD]','[UNK]']
for v in slot_tokens.values():
    slot_token_lst.extend(v)

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
        slot = [slot_token_lst.index(B_slot)] + [slot_token_lst.index(I_slot)] * max(0,len(slot)-1)
        tgt = [1]*(len(pref) + 1) + slot + [1]*(len(suff) + 1) # 1 is for [CLS] and [SEP] and [1] is [UNK] in slot
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
                "Increase the volume by ", "Decrease the volume by ","volume ","brightness ",
                "make the screen dim to ","dim the screen by "]
    slots = ['10','12','23','34','56','78','91','100']
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Quantity', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])

    # Search Query
    prefixes = ['Search for ', 'Youtube search for ', 'Search related articles for ',
                'generate images for ','Search for images related to ', 'I want images of the ',
                'search for related video ']
    slots = ['Ai','Python','Java','home tutorials','how to play chess','how earn money faster',
             "DIY tips and tricks",'how to foucs on study?','cooking',
             ]
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Query', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])

    # Youtube Search Queries
    prefixes = ["Show me videos regarding ",
               "search for videos related to ", "I need videos related to ", "videos realted to ",
               "videos of ", "Show me the videos similar to ", "Youtube search about ", "online videos on ", "YT shorts of ",
               "search any videos with tag ", "Youtube video about ","youtube ","YouTube "]
    slots = ['funny', 'jokes', 'python tutorials', 'java tutorials', 'c tutorials', 'breakfast', ' travel', 'vlogs',
              'Photography', "How to tie a tie", "Python tutorial", "Funny cat videos", "Healthy breakfast recipes", "Travel vlogs",
               "DIY home decor", "Latest movie trailers", "Workout routines", "Cake decorating ideas",
               "Photography tips", "Artificial intelligence explained", "Fashion trends", "Budget travel tips",
               "Beginner's guide to cooking", "Learn a new language", "Home workout without equipment",
               "Productivity hacks", "Music theory basics", "Tech reviews", "Home gardening tips",
               "dsa courses", "comedy videos"]
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Query', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])
    
    # Image Search Queries
    prefixes = ["Give me an image of a", "Image of a", "Show me pictures of", "Find me an image of a tropical", "I need a picture of a mountain", 
               "Can you provide an image of a", "I'm looking for pictures of", "Image search:", "Please show me photos of", 
               "Find an image related to", "search this image", "images of ", "I need images for ", "related images for ",
               "Give me the images of ", "get the image results for "]
    slots = ["cat", "sunset", "dogs", "tropical beach", "mountain landscape", "happy family", "famous landmarks", "beautiful flowers", "city skylines", "technology",
                  "human","rats","college","metro","flights","auto",'cab','car','comb','cost','country','currency','note','book',
                  'comics']
    res = combine_data(prefixes, slots, suffixes, 'Query', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])
    
    prefixes = ['search ','get ']
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

    # Location Related
    prefixes = ['get the co ordinates of ', 'co-ords of ','latitude and longitude of ','location of ',
               'geo location of ', 'I need the co-ords of ',
               'I need the location of ', 'find the location of ', 'Location ','location ']
    slots = ['New Delhi','delhi','Mumbai','Kolkata','Chennai','Bangloore','Moscow','New York','Shanghai','Tokyo',
                 'Pune','Hyderabad','Islamabad','Dhaka','columbo','Australia','India','Spain','Morocco',
                 'Paris','England','oslo','toronto','Agra','Lucknow','Muzafar nagar','vijayawada','Guntur',
                 'Vishakapatnam','Vellore','tirupati','jammu','kashmir','china','pakistan','egypt',
                 'isarel','saudi arabia']
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Location', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])

    # Cases where Slot Filling is not at all needed
    prefixes = ['Why are you so shy?','I will go and get a coffee','hi','What do you think is best?',
                'Get me some coffee','You talk so nice','what is the current time?','I need the current datetime']
    slots = ['']
    suffixes = ['']
    res = combine_data(prefixes, slots, suffixes, 'Query', split)
    train_dataset.extend(res[0])
    test_dataset.extend(res[1])

    # Open a website
    prefixes = ['Open ',"Why don't you open the ",'I want you to open ']
    slots = ['leetcode','google','bing','facebook','instagram','ibm']
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

def slot_decode( lst ):
    res = ''
    for idx in lst:
        if idx < len(slot_token_lst) and idx > 0:
           res += ' ' + slot_token_lst[idx]
        else:
           res += ' [UNK]'
    return res

def extract_slot( pred, dec ):
    assert len(pred) == len(dec)
    res = []
    for i in range(len(dec)):
        # Single slot assumed
        if dec[i] < len(slot_token_lst) and dec[i] > 0 and dec[i] != 0:
            res.append(pred[i])
    return res

print('Slots Identified:',len(slot_token_lst))
print('\n\nExample of this conversion:')
print([tokenizer.decode(train_data[0][0]), slot_decode(train_data[0][1])])
print(tokenizer.decode(extract_slot(train_data[0][0], train_data[0][1])))

print('\nWriting to csv files')
for i in ('train','val'):
    with open(f'C://users/Anirudh/Desktop/TAG_slot_filling_v0_{i}.csv','w', newline='') as f:
        csv.writer(f).writerows(train_data if i == 'train' else test_data)