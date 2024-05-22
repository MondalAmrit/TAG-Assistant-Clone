import csv, random
# from protocol_activator import protocol_map_str
ActionMap = ['Create','Read','Update','Delete']
IntentName = "Notes"

def generate_dataset(split = 0.9):
    """ Generates the dataset """
    #####################################
    # Actually this is not a correct method coz .csv is not considered.
    # But we can ignore it for now.
    # Open dataset.csv and get it's contents (Not done yet)
    
    # Add Synthetic data generation
    return generate_synthetic_dataset(split = split)

def create_examples( queries,SlotValues,TAG, split = 0.9 ):
    """ Creates dataset for the given actions based on queries and Slot Values """
    if TAG not in ActionMap:
        print('This is not a valid TAG name')
        return
    dataset = []
    for q in queries:
        for sv in SlotValues:
            dataset.append([q,f'{IntentName} {TAG}',sv])
    split_idx = int(len(dataset)*split)
    random.shuffle(dataset)
    return [dataset[:split_idx],dataset[split_idx:]]

def generate_synthetic_dataset(split = 0.9):
    """ Write down you synthetic examples here """
    dataset = [[],[]]
    # Create a New Notes
    queries = ["create a new notes","Just create a new note","I want a new note",
               "New note needed","Why don't you create a new note?"]
    tokens = [{}]
    res = create_examples( queries,tokens,'Create',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    queries = ["create a new note with name as {Query}","A new note {Query}",
               "create a Note as {Query}","create a {Query} list","new {Query} note"]
    tokens = ['shopping','groceries','cooking','important','resume','others','business']
    r = [{"Queries":i} for i in tokens]
    res = create_examples( queries,r,'Create',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]