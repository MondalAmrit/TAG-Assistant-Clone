# from protocol_activator import protocol_map_str
import random
ActionMap = ['Search']
IntentName = "YouTube"

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
    # Search prompts
    queries = ["Why don't you search for {Query} videos", "open {Query} video in youtube", "Show me videos regarding {Query}",
               "search for videos related to {Query}", "I need videos related to {Query}", "videos realted to {Query}",
               "videos of {Query}", "play {Query} on youtube", "I think its better if you can search for {Query} on YouTube",
               "Show me the videos similar to {Query}", "Youtube search about {Query}", "online videos on {Query}", "YT shorts of {Query}",
               "search any videos with tag {Query}", "Youtube video about {Query}","{Query} videos","{Query} youtube",
                "YouTube {Query}",'{Query} in YouTube','hmm. ohk now lets search for {Query} in youtube']
    tokens = ['funny', 'jokes', 'python tutorials', 'java tutorials', 'c tutorials', 'breakfast', ' travel', 'vlogs',
              'Photography', "How to tie a tie", "Python tutorial", "Funny cat videos", "Healthy breakfast recipes", "Travel vlogs",
               "DIY home decor", "Latest movie trailers", "Workout routines", "Cake decorating ideas",
               "Photography tips", "Artificial intelligence explained", "Fashion trends", "Budget travel tips",
               "Beginner's guide to cooking", "Learn a new language", "Home workout without equipment",
               "Productivity hacks", "Music theory basics", "Tech reviews", "Home gardening tips",
               "dsa courses"]
    r = [{"Query":i} for i in tokens]
    res = create_examples( queries,r,'Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]