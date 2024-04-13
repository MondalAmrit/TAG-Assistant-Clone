import csv, re
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

def get_dataset(limit =  None):
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
    return dataset

# def generate_data(prompts, intent, responses):
#     dataset = []
#     for prompt in prompts:  
#         for response in responses:  
#             dataset.append([prompt, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {intent} </INTENT>", "<TEXT>" + response + "</TEXT>"])
#     return dataset 

def getSyntheticData():
    """
    Add Your Synthetic Data here and normal data in the csv file
    """
    dataset = []

    # information
    info_prompts = ["Find information about", "Tell me about", "Provide details about", "Explain the concept of", "What is the history of", "Provide information about"]
    info_keys = ["climate change", "artificial intelligence", "COVID-19?", "space exploration", "renewable energy", "ancient civilizations", "famous scientists", "global economic trends", "theory of relativity", "effects of deforestation"]
    for p in info_prompts:
        for k in info_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['information']} </INTENT> <PARAMS>query={p+k}</PARAMS><TEXT>Searching the web...</TEXT>"])

    # open urls
    url_prompts = ['open ', 'can you please open ', 'I think its better to open ', "why don't you open ", 'please open ','Just open ']
    web_keys = ['leetcode', 'linkedin', 'amazon', 'github', 'google', 'gmail', 'geeksforgeeks', 'stackoverflow', 'netflix', 'codechef']
    for p in url_prompts:
        for k in web_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['open website']} </INTENT> <PARAMS>url={k}</PARAMS><TEXT>Opening {k}...</TEXT>"])

    # image
    image_prompts = ["Give me an image of a ", "Image of a ", "Show me pictures of ", "Find me an image of a tropical ", "I need a picture of a mountain ", "Can you provide an image of a ", "I'm looking for pictures of ", "Image search: ", "Please show me photos of ", "Find an image related to "]
    image_keys = ["cat", "sunset", "dogs", "tropical beach", "mountain landscape", "happy family", "famous landmarks", "beautiful flowers", "city skylines", "technology"]
    for p in image_prompts:
        for k in image_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['image']} </INTENT> <PARAMS>query={p+k}</PARAMS><TEXT>Generating image of {k}...</TEXT>"])

    # product
    product_prompts = ["Show me ", "Tell me about ", "Can you provide details ", "Give me information about ", "Provide information about ", "Give me details about ", "Show me available "]
    product_keys = ["latest smartphones on the market", "designer handbags.", "laptops", "sports shoes", "kitchen appliances", "luxury watches", "home decor items", "gaming consoles", "fitness trackers", "skincare products"]
    for p in product_prompts:
        for k in product_keys:
            dataset.append([p+k, f"<INTENT> {protocol_map_str['InternetSearchProtocol']} {IntentMap['product']} </INTENT> <PARAMS>product={k}</PARAMS><TEXT>Showing {k}...</TEXT>"])

    return dataset