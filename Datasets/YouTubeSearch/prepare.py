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
            dataset.append([q, f'<INTENT> {protocol_map_str["YouTubeSearchProtocol"]} {intentMap["SearchYoutube"]} </INTENT> <PARAMS> query={q} </PARAMS> <TEXT> Searching on YouTube </TEXT>'])
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
