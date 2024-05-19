import csv, random
# from protocol_activator import protocol_map_str

def get_dataset(split = 0.9, limit =  None):
    """ Generates the dataset """
    dataset = [[],[]]
    # Open dataset.csv and get it's contents (Not done yet)
    
    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        res = synthetic_examples_dataset(split = split)
        dataset[0].extend(res[0])
        dataset[1].extend(res[1])
    return dataset[0], dataset[1]

def create_examples( queries,tokens,TAG, split = 0.9 ):
    """ Creates dataset for the given actions based on queries and tokens """
    dataset = []
    for q in queries:
        for t in tokens:
            dataset.append([q.replace('#tkn#',t,1),TAG])
    split_idx = int(len(dataset)*split)
    random.shuffle(dataset)
    return [dataset[:split_idx],dataset[split_idx:]]

def synthetic_examples_dataset(split = 0.9):
    """ Write down you synthetic examples here """
    dataset = [[],[]]
    # Create a New Notes
    queries = ["create a new notes","Just create a new note","I want a new note",
               "New note needed","Why don't you create a new note?"]
    tokens = ['']
    res = create_examples( queries,tokens,'Create Notes',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    queries = ["create a new note with name as #tkn#","A new note #tkn#",
               "create a Note as #tkn#","create a #tkn# list","new #tkn# note"]
    tokens = ['shopping','groceries','cooking','important','resume','others']
    res = create_examples( queries,tokens,'Create Notes',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]