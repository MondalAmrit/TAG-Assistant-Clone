import csv, re, random
from protocol_activator import protocol_map_str

intentMap = {'SearchYoutube':1,}


def rephrase(l):
    patterns = {f'#{k}#':v for k,v in intentMap.items()}
    patterns['#PROTOCOL_CODE#'] = protocol_map_str['WeatherProtocol']

    for i in l:
        for k,v in patterns.items():
            i[1] = re.sub(k,str(v),i[1])
    return l

def get_dataset(split = 0.9, limit =  None):
    """
    Generates the dataset
    """
    dataset = []
    # Open dataset.csv and get it's contents
    with open('Datasets/WeatherForecast/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = rephrase(list(reader)[:limit] if limit else list(reader))
    
    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())
        
    split_idx = int(split*len(dataset))
    random.shuffle(dataset)
    return dataset[:split_idx], dataset[split_idx:]


def generate_data(query):
    dataset = []
    for q in query:
            dataset.append([f'Search {q} on Youtube', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'Search for {q} on YouTube', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'Search {q} on YT', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'Youtube search for {q}', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'Youtube search on {q}', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'Youtube search about {q}', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'search in youtube for {q}', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'{q} in YouTube', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'Videos of {q} from YouTube', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
            dataset.append([f'Youtube Playlists for {q}', f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>', "YouTubeSearchProtocol search Youtube"])
    return dataset


def getSyntheticData():
    """
    Generates the Synthetic dataset
    """
    dataset = []
    
    # Videos
    queries = ["How to tie a tie", "Python tutorial", "Funny cat videos", "Healthy breakfast recipes", "Travel vlogs",
               "DIY home decor", "Latest movie trailers", "Workout routines", "Cake decorating ideas",
               "Photography tips", "Artificial intelligence explained", "Fashion trends", "Budget travel tips",
               "Beginner's guide to cooking", "Learn a new language", "Home workout without equipment",
               "Productivity hacks", "Music theory basics", "Tech reviews", "Home gardening tips"]
    dataset.extend(generate_data(queries))

    # Creators
    queries = ["PewDiePie", "T-Series", "MrBeast", "Dude Perfect", "5-Minute Crafts", "Markiplier", "Jenna Marbles",
               "Smosh", "Rhett & Link", "Ryan's World", "Good Mythical Morning", "Jake Paul", "Ninja", "James Charles",
               "David Dobrik", "Liza Koshy", "Casey Neistat", "Emma Chamberlain", "Lilly Singh", "The Try Guys"]
    dataset.extend(generate_data(queries))
    return dataset

def create_examples( queries,tokens,TAG,prompt_only=False ):
    dataset = []
    for q in queries:
        for t in tokens:
            if prompt_only:
                dataset.append(q.replace('#tkn#',t,1))
            else:
                dataset.append([q.replace('#tkn#',t,1),TAG])
    return dataset

def synthetic_examples_dataset():
    dataset = []
    # Search prompts
    queries = ["Why don't you search for #tkn# videos", "open #tkn# video in youtube", "Show me videos regarding #tkn#",
               "search for videos related to #tkn#", "I need videos related to #tkn#", "videos realted to #tkn#",
               "videos of #tkn#", "play #tkn# on youtube"]
    tokens = ['funny', 'jokes', 'python tutorials', 'java tutorials', 'c tutorials', 'breakfast', ' travel', 'vlogs',
              'Photography']
    
    dataset.extend(create_examples( queries,tokens,'YouTube Search' ))
