import csv, re, random
from protocol_activator import protocol_map_str

IntentMap = {
    "information" : 1,
    "open website" : 2,
    "image" : 3,
    "product" : 4,
}

def rephrase(l):
    patterns = {f'#{k}#':v for k,v in IntentMap.items()}
    patterns['#PROTOCOL_CODE#'] = protocol_map_str['InternetSearchProtocol']

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
    with open('Datasets/InternetSearch/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = list(reader)[:limit] if limit else list(reader)

    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())

    split_idx = int(split*len(dataset))
    random.shuffle(dataset)
    return dataset[:split_idx], dataset[split_idx:]

def getSyntheticData():
    dataset = []

    # information
    info_prompts = ["Find information about","Tell me about","Provide details about",
                    "Explain the concept of","What is the history of","Provide information about",
                    "Could you enlighten me on","I'm curious about","Can you shed some light on",
                    "Give me insights into","I'd like to explore","Help me understand",
                    "I'm interested in learning about","Share some knowledge about","Can you delve into",
                    "Clarify the significance of","I want to know more about","Unravel the mysteries of",
                    "Educate me on","Could you elucidate","Brief me on","Give me an overview of",
                    "I'm eager to discover","Could you provide some background on","Let's delve into the details of",
                    "Enlighten me about","Elaborate on",]
    info_keys = ["climate change", "artificial intelligence", "COVID-19?", "space exploration", "renewable energy", "ancient civilizations", "famous scientists", "global economic trends", "theory of relativity", "effects of deforestation",
                "the mysteries of the deep sea",
                "the wonders of the Amazon rainforest", "the future of renewable energy technologies", "the psychology behind decision-making processes",
                "the impact of AI on creative industries",    "the evolution of space exploration",    "the cultural significance of ancient ruins",    
                "the intersection of art and technology",    "the benefits of sustainable living practices",    "the history of fashion and its societal impacts",    
                "the future of genetic engineering",    "the role of storytelling in human history",    "the mysteries of the cosmos",    "the psychology of fear and anxiety",    
                "the impact of social media activism",    "the future of augmented reality",    "the history of human migration patterns",    "the ethical implications of gene editing",    
                "the benefits of green urban planning",    "the evolution of human communication",    "the psychology of memory and cognition",    
                "the impact of colonialism on indigenous cultures",    "the future of quantum computing",    "the history of cryptography and code-breaking",    
                "the cultural significance of traditional music",    "the benefits of mindfulness meditation practices",    "the psychology of addiction and recovery",    
                "the impact of climate change on indigenous communities",    "the future of 3D printing technology",    "the history of medical breakthroughs",    
                "the intersection of science and spirituality",    "the benefits of intercultural exchange programs",    "the psychology of altruism and empathy",    
                "the impact of artificial intelligence on healthcare",    "the future of wearable technology",    "the history of protest movements",    
                "the cultural significance of culinary traditions",    "the benefits of green energy initiatives",    "the psychology of dreams and unconscious thought",    
                "the impact of automation on the future of work",    "the future of space tourism",    "the history of human rights movements",
                "the cultural significance of traditional ceremonies", "the benefits of community gardening projects",
                "the psychology of personality development","the impact of globalization on local economies", "the future of personalized medicine",
                "the history of environmental conservation efforts", "the cultural significance of street art", "the benefits of collaborative research initiatives",
                "maths","physics","chemistry","sicence","computers","ecology","geography","data analytics","ai","llm","language models"]
    for p in info_prompts:
        for k in info_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['information']} </INTENT> <PARAMS> query={p+k} </PARAMS> <TEXT> Searching the web... </TEXT>"])

    # open urls
    # URL prompts with expansions
    url_prompts = ['open ', 'can you please open ', 'I think its better to open ', "why don't you open ", 'please open ', 'Just open ',
                'Navigate to ', 'Launch ', 'Go to ', 'Visit ', 'Access ', 'Take me to ', 
                'Direct me to ', 'Load ', 'Explore ', 'Check out ']

    # Web keys with expansions
    web_keys = ['leetcode', 'linkedin', 'amazon', 'github', 'google', 'gmail', 'geeksforgeeks', 'stackoverflow', 'netflix', 'codechef',
                'youtube', 'facebook', 'twitter', 'instagram', 'wikipedia', 'reddit', 'quora', 'ebay', 'microsoft', 'apple',
                'spotify', 'bbc', 'cnn', 'nytimes', 'yahoo', 'bing', 'wordpress', 'pinterest', 'dropbox', 'twitch']
    for p in url_prompts:
        for k in web_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['open website']} </INTENT> <PARAMS> url={k} </PARAMS> <TEXT> Opening {k}... </TEXT>"])

    # image
    image_prompts = ["Give me an image of a ", "Image of a ", "Show me pictures of ", "Find me an image of a tropical ", "I need a picture of a mountain ", "Can you provide an image of a ", "I'm looking for pictures of ", "Image search: ", "Please show me photos of ", "Find an image related to "]
    image_keys = ["cat", "sunset", "dogs", "tropical beach", "mountain landscape", "happy family", "famous landmarks", "beautiful flowers", "city skylines", "technology",
                  "human","rats","college","metro","flights","auto",'cab','car','comb','cost','country','currency','note','book']
    for p in image_prompts:
        for k in image_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['image']} </INTENT> <PARAMS> query={p+k} </PARAMS> <TEXT> Generating image of {k}... </TEXT>"])

    # product
    product_prompts = ["Show me ","Show me the products related to " , "Tell me about ", "Can you provide details ", "Give me information about ", "Provide information about ", "Give me details about ", "Show me available ",
                    "What are the options for ", "I'm interested in ", "Please display ", "Could you show me ", "I'd like to see ", "I'm looking for details on ",
                    "Please provide info on ", "Can you show me ", "What's available for ", "Related products for ",
                    "Product options for ",'Amazon search for ']

    product_keys = ["latest smartphones on the market", "designer handbags", "laptops", "sports shoes", "kitchen appliances", "luxury watches", "home decor items",
                    "gaming consoles", "fitness trackers", "skincare products", "smart home devices", "office chairs", "travel accessories", "headphones",
                    "outdoor furniture", "camera equipment", "pet supplies", "books", "gourmet food items", "fashion accessories", "DIY tools", "art supplies",
                    "baby products", "musical instruments", "sporting goods", "car accessories", "gardening tools", "cooking utensils", "party supplies",
                    "samsung s20 ultra", 'IQOO Z6 lite','realme 9','realme 8i','xiaomi','redmi','poco','pocox2','Noise fit']
    for p in product_prompts:
        for k in product_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['product']} </INTENT> <PARAMS> product={k} </PARAMS> <TEXT> Showing {k}... </TEXT> "])

    return dataset