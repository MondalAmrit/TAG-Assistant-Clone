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
        "Convert {FileType} to {TargetType}", "Please convert {FileType} to {TargetType}", 
        "Can you convert {FileType} to {TargetType}", "Convert my {FileType} to {TargetType}", 
        "Change {FileType} to {TargetType}", "Transform {FileType} to {TargetType}", 
        "I need to convert {FileType} to {TargetType}", "Please change {FileType} to {TargetType}", 
        "Convert this {FileType} file to {TargetType}", "Can you change {FileType} to {TargetType}"
    ]
    
    file_types = ["Word document", "Excel spreadsheet", "PDF", "PNG image", "JPEG image", "PowerPoint slide"]
    target_types = ["PDF", "Word document", "Excel spreadsheet", "PNG image", "JPEG image", "PowerPoint slide"]
    
    r = [{"FileType": ft, "TargetType": tt} for ft in file_types for tt in target_types if ft != tt]
    res = create_examples(queries, r, 'ConvertFile', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]
