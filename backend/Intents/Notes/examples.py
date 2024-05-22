###################################################
# Open the notes can be considered as new feature
# Update File add Description to item can be considered in future updates
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
               "create a Note as {Query}","create a {Query} list","new {Query} note",
               "Let's start with creating {Query}","create {Query} list","New {Query} list",
               "New note as {Query}"]
    tokens = ['shopping','groceries','cooking','important','resume','others','business']
    r = [{"Query":i} for i in tokens]
    res = create_examples( queries,r,'Create',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Read notes
    queries = ["what's in the {Query}","Read out the {Query} notes",
               "{Query} list"," I want you to open the {Query} notes",
               "Open the {Query} list","Show me the {Query} list", "Why don't you open the {Query} notes"]
    res = create_examples( queries,r,'Read',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Update Notes
    # 3 cases :
    # 1. Add New Item
    # 2. Modify Existing Item
    # 3. Add to existing Item
    # 4. Remove Existing Item
    
    # 1. Add New Item
    queries = ['Add {Query_1} to {Query_2} list',"New Item {Query_1} in {Query_2} notes"]
    q1 = ['Sauce','Gulab Jamun','Spoon','Stuff','Milk', 'Eggs', 'Bread', 'Sugar','Pasta', 'Rice', 'Chicken', 'Salad']
    q2 = ['Cooking','Shopping','Groceries','To Buy']
    r = []
    for i in q1:
        for j in q2:
            r.append({"Query_1":i,"Query_2":j})
    res = create_examples( queries,r,'Update',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # 2. Modify Existing Item
    queries = ['Change {Query_1} in {Query_2} list to {Query_3}','Replace {Query_1} in {Query_2} list with {Query_3}', 
               'Update {Query_2} list by changing {Query_1} to {Query_3}', 'Switch {Query_1} in {Query_2} list to {Query_3}']
    q1 = ['Milk', 'Eggs', 'Bread', 'Sugar','Pasta', 'Rice', 'Chicken', 'Salad']
    q2 = ['Shopping', 'Groceries', 'To Buy','Spaghetti', 'Brown Rice', 'Tofu', 'Caesar Salad']
    new_items = ['Almond Milk', 'Organic Eggs', 'Whole Wheat Bread', 'Brown Sugar']
    r = []
    for item in q1:
        for category in q2:
            for new_item in new_items:
                r.append({"Query_1": item, "Query_2": category, "Query_3": new_item})
    res = create_examples(queries, r, 'Update', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # 3. Add to existing Item
    queries = ['Include {Query_3} in {Query_2} list with description {Query_1}', 'Add {Query_1} about {Query_3} to {Query_2} list', 'Append {Query_1} to {Query_3} in {Query_2} list']
    new_items = ['Olive Oil', 'Apple Cider Vinegar', 'Quinoa', 'Hummus']
    descriptions = ['for salad dressing', 'for marinating', 'for side dish', 'for dipping']
    q2 = ['Recipes', 'Ingredients', 'Cooking']
    r = []
    for new_item in new_items:
        for description in descriptions:
            for category in q2:
                r.append({"Query_3": new_item, "Query_1": description, "Query_2": category})
    res = create_examples(queries, r, 'Update', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # 4. Remove Existing Item
    queries = ['Remove {Query_1} from {Query_2} list']
    q1 = ['Apples', 'Oranges', 'Bananas', 'Tomatoes']
    q2 = ['Fruits', 'Groceries', 'To Buy']
    r = []
    for item in q1:
        for category in q2:
            r.append({"Query_1": item, "Query_2": category})
    res = create_examples(queries, r, 'Update', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Delete Notes
    queries = ['Delete {Query} list', 'Remove {Query} notes', 'Erase {Query}',
               'Clear {Query} list', 'Wipe out {Query} notes', 'Purge {Query}', 'Erase all items from {Query} list']
    q = ['To Do', 'shopping','groceries','cooking','important','resume','others','business']
    r = [{"Query": i} for i in q]
    res = create_examples(queries, r, 'Delete', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])


    return dataset[0], dataset[1]

res = generate_synthetic_dataset()