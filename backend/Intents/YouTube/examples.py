from protocol_activator import protocol_map_str

intentMap = {'Youtube Search':1,}

def get_dataset(split = 0.9, limit =  None):
    """ Generates the dataset """
    dataset = []
    # Open dataset.csv and get it's contents (Not done yet)
    
    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        res = synthetic_examples_dataset(split = split)
        dataset[0].extend(res[0])
        dataset[1].extend(res[1])
        
    return dataset[0], dataset[1]

def create_examples( queries,tokens,TAG, split = 0.9 ):
    """ Creates dataset for the given actions based on queries and tokens """
    dataset = []
    for q in queries:
        for t in tokens:
            dataset.append([q.replace('#tkn#',t,1),TAG])
    split_idx = int(len(dataset)*split)
    return [dataset[:split_idx],dataset[split_idx:]]

def synthetic_examples_dataset(split = 0.9):
    """ Write down you synthetic examples here """
    dataset = []
    # Search prompts
    queries = ["Why don't you search for #tkn# videos", "open #tkn# video in youtube", "Show me videos regarding #tkn#",
               "search for videos related to #tkn#", "I need videos related to #tkn#", "videos realted to #tkn#",
               "videos of #tkn#", "play #tkn# on youtube", "I think its better if you can search for #tkn# on YouTube",
               "Show me the videos similar to #tkn#", "Youtube search about #tkn#", "online videos on #tkn#", "YT shorts of #tkn#"]
    tokens = ['funny', 'jokes', 'python tutorials', 'java tutorials', 'c tutorials', 'breakfast', ' travel', 'vlogs',
              'Photography', "How to tie a tie", "Python tutorial", "Funny cat videos", "Healthy breakfast recipes", "Travel vlogs",
               "DIY home decor", "Latest movie trailers", "Workout routines", "Cake decorating ideas",
               "Photography tips", "Artificial intelligence explained", "Fashion trends", "Budget travel tips",
               "Beginner's guide to cooking", "Learn a new language", "Home workout without equipment",
               "Productivity hacks", "Music theory basics", "Tech reviews", "Home gardening tips"]
    
    res = create_examples( queries,tokens,'YouTube Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
