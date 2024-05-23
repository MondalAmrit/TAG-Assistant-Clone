######################################################
# It would be better to consider the news preferances
# Also providing the summary can be a good option
# Option for selecting news sources is not implemented

import random
ActionMap = ['Latest']
IntentName = "News"

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

    queries = ["get the latest news","what's happening?","What is in the headlines?",
               "show me the news","news headlines","latest news"]
    tokens = [{}]
    res = create_examples( queries,tokens,'Latest',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    queries = ["What's happening in the {Query} world?","I need {Query} news",
               "headlines related to {Query}"]
    tokens = [{"Query":i} for i in ["Tech","politics","Business","METRO cities","Cinema","Health","International","National"]]
    res = create_examples( queries,tokens,'Latest',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]