import csv, random
from protocol_activator import protocol_map_str

# Git Command Intent Map
IntentMap = {
    "initialize repository": 1,
    "add files": 2,
    "commit changes": 3,
    "check status": 4,
    "view log": 5,
    "list branches": 6,
    "create branch": 7,
    "checkout branch": 8,
    "merge changes": 9,
    "add remote": 10,
    "remove remote": 11,
    "push changes": 12,
    "pull changes": 13,
    "create tag": 14,
    "add interactive": 15,
    "remove file": 16,
    "ignore file": 17,
    "undo changes": 18,
    "fetch changes": 19,
    "rebase branch": 20,
    "view differences": 21,
    "show staged changes": 22,
    "stash changes": 23,
    "pop stash": 24,
    "cherry-pick commit": 25
}

def get_dataset(split = 0.9, limit =  None):
    """
    Generates the dataset
    """
    dataset = []
    # Open dataset.csv and get it's contents
    with open('Datasets/GITcommandHandler/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = list(reader)[:limit] if limit else list(reader)

    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())
    split_idx = int(split*len(dataset))
    random.shuffle(dataset)
    return dataset[:split_idx], dataset[split_idx:]

def get_data(commands, prompts, intent):
    """
    Generate data based on commands and prompts.
    """
    dataset = []
    for command in commands:
        for prompt in prompts:
            dataset.append([prompt.replace('#TKN#',command), f"<INTENT> {protocol_map_str['GITCommandProtocol']} {IntentMap[intent]} </INTENT> <PARAMS> command={command} </PARAMS>"])
    return dataset

def getSyntheticData():
    """
    Add Your Synthetic Data here and normal data in the csv file
    """
    dataset = []

    # Add Files to a repo
    commands = [f'file{i}.py' for i in range(20)] + ['file.py','sample.py','testing.txt','sample.txt']
    prompts = ['Add file #TKN#', 'Stage file #TKN#', 'Include file #TKN#', 'Append file #TKN#', 
               'Can you please add this file #TKN#', "Why don't you add #TKN#",
               'Add #TKN# file to the repo', 'Add #TKN# file']
    dataset.extend(get_data(commands, prompts, 'add files'))

    # Create new branch
    branches = ['feature-branch', 'bug-fix-branch', 'hotfix-branch','test-branch','error-branch']
    prompts = ['Create branch #TKN#', 'Make branch #TKN#', 'Establish branch #TKN#', 'Generate branch #TKN#',]
    projects= ['TAG','Protfolio','project A','project B','management tools','Somethings project']
    prompts.extend([f'Can you create a new branch in {i} as #TKN#' for i in projects])
    dataset.extend(get_data(branches, prompts, 'create branch'))

    # For Remote
    remotes = ['origin', 'upstream', 'forked']
    prompts = ['Add remote #TKN#', 'Include remote #TKN#', 'Connect remote #TKN#', 'Link remote #TKN#',
               'Can you please add remote in github #TKN#', "Why don't you add remote in github #TKN#",
               "I think its better to add #TKN# to github", 'git remote #TKN#']
    dataset.extend(get_data(remotes, prompts, 'add remote'))

    #
    tags = ['v1.0', 'v2.0', 'release-1.0', 'beta-2.0']
    prompts = ['Create tag #TKN#', 'Generate tag #TKN#', 'Label tag #TKN#', 'Mark tag #TKN#',
               'Can you create a tag in github as #TKN#', 'create a tag  in github as #TKN#',
               'create a new tag in github with name #TKN#', "Why don't you create a tag with name as #TKN#",
               'create a #TKN# tag', 'make a #TKN# tag']
    dataset.extend(get_data(tags, prompts, 'create tag'))

    return dataset