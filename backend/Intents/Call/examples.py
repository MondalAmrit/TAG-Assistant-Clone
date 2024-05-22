import csv, random

ActionMap = ['MakeCall','PickCall','CutCall']
IntentName = "Call"

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
        print('This is not a valid TAG name: ', TAG)
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

    # Call
    queries = [
        "Call {Query}", "Please call {Query}", "Can you call {Query}", "Dial the number of {Query}", "Dial {Query}",
        "Call the number of {Query}", "Can you call the number of {Query}", "Call the number {Query}",
        "Can you call the number {Query}", "I want you to call {Query}", "I want you to call the number of {Query}",
        "I want you to dial the number of {Query}", "I want you to dial {Query}", "Hit {Query} up",
        "Hit the number of {Query}", "Ring up {Query}", "Ring up the number of {Query}", "Can you ring {Query}",
        "Can you ring up {Query}", "Call {Query} now", "Please give {Query} a call", "Can you give {Query} a ring?",
        "Dial up {Query}", "Dial {Query}'s number", "Call up the number of {Query}",
        "Can you give a call to the number of {Query}?", "Call this number: {Query}", "Can you call this person: {Query}?",
        "I need you to call {Query}", "I want you to call {Query}'s number", "I need you to dial {Query}'s number",
        "I want you to dial this person: {Query}", "Hit up {Query}", "Hit the number of {Query}", "Ring {Query} up",
        "Ring up {Query}'s number", "Can you ring up {Query}?", "Can you ring up this person: {Query}?",
    ]
    names = ["Anirudh Mukkamala","Rishav Raj","Amritapa Mondal","Vikram Singh Chauhan","Vaibhav Garg",
             "Ansh Gupta","Ansh Goyal","Rishabh Chaudhary","Shubham Kumar Singh","Hardik Gupta","Jane Foster",
             "Tony Stark","Donald Trump","Barak Obama","Narendra Modi","Mukesh Ambani"]
    r = [{"Query":i} for i in names]
    res = create_examples( queries,r,'MakeCall',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # PickCall
    queries = [
        "Pick up the call", "Can you pick up the call?", "Pick up the call now", "Pick up the call right now",
        "Please pick up the call", "Answer the call", "Can you answer the call?", "Answer the call now",
        "Answer the call right now", "Please answer the call", "Take the call", "Can you take the call?",
        "Take the call now", "Take the call right now", "Please take the call", "Grab the call",
        "Can you grab the call?", "Grab the call now", "Grab the call right now", "Please grab the call",
        "Answer the call"
    ]
    r = [{}]
    res = create_examples( queries,r,'PickCall',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # CutCall
    queries = [
        "Cut the call", "Can you cut the call?", "Cut the call now", "Cut the call right now", "Please cut the call",
        "Hang up the call", "Can you hang up the call?", "Hang up the call now", "Hang up the call right now",
        "Please hang up the call", "Hang up the call", "Can you hang up the call?", "Hang up the call now",
        "Hang up the call right now", "Please hang up the call", "End the call", "Can you end the call?",
        "End the call now", "End the call right now", "Please end the call", "Disconnect the call",
        "Can you disconnect the call?", "Disconnect the call now", "Disconnect the call right now",
        "Please disconnect the call", "Terminate the call", "Can you terminate the call?", "Terminate the call now",
        "Terminate the call right now", "Please terminate the call",
    ]
    res = create_examples( queries,r,'CutCall',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]