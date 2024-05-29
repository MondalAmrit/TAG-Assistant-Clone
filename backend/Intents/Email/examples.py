import csv, random

ActionMap = ['ReadEmail', 'SendEmail', 'SearchEmail']
IntentName = "Email"

def create_examples(queries, SlotValues, TAG, split = 0.9):
    """ Creates dataset for the given actions based on queries and Slot Values """
    if TAG not in ActionMap:
        print('This is not a valid TAG name: ', TAG)
        return
    dataset = []
    for q in queries:
        for sv in SlotValues:
            dataset.append([q,f'{IntentName} {TAG}',sv])
    split_idx = int(len(dataset) * split)
    random.shuffle(dataset)
    return [dataset[:split_idx], dataset[split_idx:]]

def generate_synthetic_dataset(split = 0.9):
    """ Write down your synthetic examples here """
    dataset = [[], []]

    # ReadEmail
    queries = [
        "Read the email from {Query}", "Can you read the email from {Query}?", "Please read the email from {Query}",
        "Show me the email from {Query}", "Open the email from {Query}", "Read the latest email from {Query}",
        "Can you open the email from {Query}?", "Please open the email from {Query}", "Show me the latest email from {Query}",
        "Open the latest email from {Query}"
    ]
    names = ["Anirudh Mukkamala","Rishav Raj","Amritapa Mondal","Vikram Singh Chauhan","Vaibhav Garg",
             "Ansh Gupta","Ansh Goyal","Rishabh Chaudhary","Shubham Kumar Singh","Hardik Gupta","Jane Foster",
             "Tony Stark","Donald Trump","Barak Obama","Narendra Modi","Mukesh Ambani"]
    r = [{"Query": i} for i in names]
    res = create_examples(queries, r, 'ReadEmail', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # SendEmail
    queries = [
        "Send an email to {Query}", "Please send an email to {Query}", "Can you send an email to {Query}",
        "Email {Query}", "Send a message to {Query}", "Compose an email to {Query}", "Write an email to {Query}",
        "Can you compose an email to {Query}?", "Please compose an email to {Query}", "Send an email now to {Query}"
    ]
    r = [{"Query": i} for i in names]
    res = create_examples(queries, r, 'SendEmail', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # SearchEmail
    queries = [
        "Search for an email from {Query}", "Find an email from {Query}", "Look for an email from {Query}",
        "Locate an email from {Query}", "Search the inbox for an email from {Query}", "Can you find an email from {Query}",
        "Please search for an email from {Query}", "Show me emails from {Query}", "Can you locate an email from {Query}",
        "Please find an email from {Query}"
    ]
    r = [{"Query": i} for i in names]
    res = create_examples(queries, r, 'SearchEmail', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]
