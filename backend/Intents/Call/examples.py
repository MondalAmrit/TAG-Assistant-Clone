import csv, random

IntentMap = {
    "Call": 1,
    "PickCall": 2,
    "CutCall": 3,
}


def get_dataset(split=0.9, limit=None):
    """Generates the dataset"""
    dataset = [[], []]
    # Open dataset.csv and get it's contents (Not done yet)

    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        res = synthetic_examples_dataset(split=split)
        dataset[0].extend(res[0])
        dataset[1].extend(res[1])
    return dataset[0], dataset[1]


def create_examples(queries, tokens, TAG, split=0.9):
    """Creates dataset for the given actions based on queries and tokens"""
    dataset = []
    for q in queries:
        for t in tokens:
            dataset.append([q.replace("#tkn#", t, 1), TAG])
    split_idx = int(len(dataset) * split)
    random.shuffle(dataset)
    return [dataset[:split_idx], dataset[split_idx:]]


def synthetic_examples_dataset(split=0.9):
    """Write down you synthetic examples here"""
    dataset = [[], []]

    # Call
    queries = [
        "Call #tkn#", "Please call #tkn#", "Can you call #tkn#", "Dial the number of #tkn#", "Dial #tkn#",
        "Call the number of #tkn#", "Can you call the number of #tkn#", "Call the number #tkn#",
        "Can you call the number #tkn#", "I want you to call #tkn#", "I want you to call the number of #tkn#",
        "I want you to dial the number of #tkn#", "I want you to dial #tkn#", "Hit #tkn# up",
        "Hit the number of #tkn#", "Ring up #tkn#", "Ring up the number of #tkn#", "Can you ring #tkn#",
        "Can you ring up #tkn#", "Call #tkn# now", "Please give #tkn# a call", "Can you give #tkn# a ring?",
        "Dial up #tkn#", "Dial #tkn#'s number", "Call up the number of #tkn#",
        "Can you give a call to the number of #tkn#?", "Call this number: #tkn#", "Can you call this person: #tkn#?",
        "I need you to call #tkn#", "I want you to call #tkn#'s number", "I need you to dial #tkn#'s number",
        "I want you to dial this person: #tkn#", "Hit up #tkn#", "Hit the number of #tkn#", "Ring #tkn# up",
        "Ring up #tkn#'s number", "Can you ring up #tkn#?", "Can you ring up this person: #tkn#?",
    ]

    # PickCall
    queries = [
        "Pick up the call", "Can you pick up the call?", "Pick up the call now", "Pick up the call right now",
        "Please pick up the call", "Answer the call", "Can you answer the call?", "Answer the call now",
        "Answer the call right now", "Please answer the call", "Take the call", "Can you take the call?",
        "Take the call now", "Take the call right now", "Please take the call", "Grab the call",
        "Can you grab the call?", "Grab the call now", "Grab the call right now", "Please grab the call",
    ]

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
