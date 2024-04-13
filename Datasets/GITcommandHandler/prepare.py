import csv
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

def get_dataset(limit =  None):
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
    return dataset

def get_data(commands, prompts):
    """
    Generate data based on commands and prompts.
    """
    dataset = []
    for command in commands:
        for prompt in prompts:
            dataset.append([prompt + command, f"<INTENT> GitProtocol {IntentMap[prompt]} </INTENT><PARAMS> command={command} </PARAMS>"])
    return dataset

def getSyntheticData():
    """
    Add Your Synthetic Data here and normal data in the csv file
    """
    dataset = []

    commands = ['file1.py', 'file2.py', 'file3.py', 'file4.py', 'file5.py']
    prompts = ['Add file ', 'Stage file ', 'Include file ', 'Append file ']
    dataset.extend(get_data(commands, prompts))

    branches = ['feature-branch', 'bug-fix-branch', 'hotfix-branch']
    prompts = ['Create branch ', 'Make branch ', 'Establish branch ', 'Generate branch ']
    dataset.extend(get_data(branches, prompts))

    remotes = ['origin', 'upstream', 'forked']
    prompts = ['Add remote ', 'Include remote ', 'Connect remote ', 'Link remote ']
    dataset.extend(get_data(remotes, prompts))

    tags = ['v1.0', 'v2.0', 'release-1.0', 'beta-2.0']
    prompts = ['Create tag ', 'Generate tag ', 'Label tag ', 'Mark tag ']
    dataset.extend(get_data(tags, prompts))

    return dataset