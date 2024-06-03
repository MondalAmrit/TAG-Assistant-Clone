import csv, random

ActionMap = ['ConvertFile']
IntentName = "FileConversion"

def generate_dataset(split=0.9):
    """Generates the dataset"""
    return generate_synthetic_dataset(split=split)

def create_examples(queries, SlotValues, TAG, split=0.9):
    """Creates dataset for the given actions based on queries and Slot Values"""
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

def generate_synthetic_dataset(split=0.9):
    """Write down your synthetic examples here"""
    dataset = [[], []]

    # ConvertFile
    queries = [
        "Convert {Query_1} to {Query_2}", "Please convert {Query_1} to {Query_2}", 
        "Can you convert {Query_1} to {Query_2}", "Convert my {Query_1} to {Query_2}", 
        "Change {Query_1} to {Query_2}", "Transform {Query_1} to {Query_2}", 
        "I need to convert {Query_1} to {Query_2}", "Please change {Query_1} to {Query_2}", 
        "Convert this {Query_1} file to {Query_2}", "Can you change {Query_1} to {Query_2}"
    ]
    
    file_types = ["Word document", "Excel spreadsheet", "PDF", "PNG image", "JPEG image", "PowerPoint slide"]
    target_types = ["PDF", "Word document", "Excel spreadsheet", "PNG image", "JPEG image", "PowerPoint slide"]
    
    r = [{"Query_1": ft, "Query_2": tt} for ft in file_types for tt in target_types if ft != tt]
    res = create_examples(queries, r, 'ConvertFile', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]
