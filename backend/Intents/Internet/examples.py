import csv, re, random
# from protocol_activator import protocol_map_str

IntentMap = {
    "Information" : 1,
    "Open Website" : 2,
    "Image Search" : 3,
    "Product Search" : 4,
}

def get_dataset(split = 0.9, limit =  None):
    """ Generates the dataset """
    dataset = [[],[]]
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
    random.shuffle(dataset)
    return [dataset[:split_idx],dataset[split_idx:]]

def synthetic_examples_dataset(split = 0.9):
    """ Write down you synthetic examples here """
    dataset = [[],[]]
    # information
    queries = ["Find information about #tkn#","Tell me about #tkn#","Provide details about #tkn#",
                    "Explain the concept of #tkn#","What is the history of #tkn#","Provide information about #tkn#",
                    "Could you enlighten me on #tkn#","I'm curious about #tkn#","Can you shed some light on #tkn#",
                    "Give me insights into #tkn#","I'd like to explore #tkn#","Help me understand #tkn#",
                    "I'm interested in learning about #tkn#","Share some knowledge about #tkn#","Can you delve into #tkn#",
                    "Clarify the significance of #tkn#","I want to know more about #tkn#","Unravel the mysteries of #tkn#",
                    "Educate me on #tkn#","Could you elucidate #tkn#","Brief me on #tkn#","Give me an overview of #tkn#",
                    "I'm eager to discover #tkn#","Could you provide some background on #tkn#","Let's delve into the details of #tkn#",
                    "Enlighten me about #tkn#","Elaborate on #tkn#",
                "Internet Search for #tkn#", "Search online for #tkn#", "Search in chrome for #tkn#",
                "Search on bing for #tkn#", "search on edge for #tkn#", "Why don't you search for #tkn# in the internet?",
                "Why don't you search #tkn# in chrome", "#tkn# in internet"]
    tokens = ["climate change", "artificial intelligence", "COVID-19?", "space exploration", "renewable energy", "ancient civilizations", "famous scientists", "global economic trends", "theory of relativity", "effects of deforestation",
                "the mysteries of the deep sea", "how to open django website?", "how to host a python code?",
                "how to get rid of the bugs?",
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
                "the psychology of personality development","the impact of globalization on local economies", "the benefits of collaborative research initiatives",
                "maths","physics","chemistry","sicence","computers","ecology","geography","data analytics","ai","llm","language models"]
    res = create_examples( queries,tokens,'Information',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    
    # open urls
    queries = ['open #tkn#', 'can you please open #tkn#', 'I think its better to open #tkn#', "why don't you open #tkn#", 'please open #tkn#', 'Just open #tkn#',
                'Navigate to #tkn#', 'Launch #tkn#', 'Go to #tkn#', 'Visit #tkn#', 'Access #tkn#', 'Take me to #tkn#', 
                'Direct me to #tkn#', 'Load #tkn#', 'Explore #tkn#', 'Check out #tkn#', 'I want you to open #tkn#', "Why don't you open #tkn#?",
                "show me the #tkn#", "I want you to open #tkn#", "Hey, Why don't you open #tkn# ?", "Just open the #tkn#",
                "Open #tkn# in a browser", "Quickly open the #tkn#"]
    tokens = ['leetcode', 'linkedin', 'amazon', 'github', 'google', 'gmail', 'geeksforgeeks', 'stackoverflow', 'netflix', 'codechef',
                'youtube', 'facebook', 'twitter', 'instagram', 'wikipedia', 'reddit', 'quora', 'ebay', 'microsoft', 'apple',
                'spotify', 'bbc', 'cnn', 'nytimes', 'yahoo', 'bing', 'wordpress', 'pinterest', 'dropbox', 'twitch']
    res = create_examples( queries,tokens,'Open Website',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Image Search
    queries = ["Give me an image of a #tkn#", "Image of a #tkn#", "Show me pictures of #tkn#", "Find me an image of a tropical #tkn#", "I need a picture of a mountain #tkn#", 
               "Can you provide an image of a #tkn#", "I'm looking for pictures of #tkn#", "Image search: #tkn#", "Please show me photos of #tkn#", 
               "Find an image related to #tkn#", "search this image #tkn#", "Why don't you search for this image #tkn# on google?",
               "search this photo #tkn# on google", "search for image of #tkn# online", "images of ", "I need images for ", "related images for ",
               "Give me the images of #tkn#", "get the image results for #tkn#","#tkn# images"]
    tokens = ["cat", "sunset", "dogs", "tropical beach", "mountain landscape", "happy family", "famous landmarks", "beautiful flowers", "city skylines", "technology",
                  "human","rats","college","metro","flights","auto",'cab','car','comb','cost','country','currency','note','book']
    res = create_examples( queries,tokens,'Image Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # product
    queries = ["Show me #tkn#","Show me the products related to #tkn#" , "Tell me about #tkn#", "Can you provide details #tkn#", "Give me information about #tkn#", "Provide information about #tkn#", "Give me details about #tkn#", "Show me available #tkn#",
                    "What are the options for #tkn#", "I'm interested in #tkn#", "Please display #tkn#", "Could you show me #tkn#", "I'd like to see #tkn#", "I'm looking for details on #tkn#",
                    "Please provide info on #tkn#", "Can you show me #tkn#", "What's available for #tkn#", "Related products for #tkn#",
                    "Product options for #tkn#",'Amazon search for #tkn#', "search for the #tkn# online", "get me the #tkn# products",
                    "Why don't you get me the product related to #tkn#", "Show me the prices for the #tkn#",
                    "latest #tkn#","#tkn# new models","brand new #tkn#"]

    tokens = ["smartphones on the market", "designer handbags", "laptops", "sports shoes", "kitchen appliances", "luxury watches", "home decor items",
                    "gaming consoles", "fitness trackers", "skincare products", "smart home devices", "office chairs", "travel accessories", "headphones",
                    "outdoor furniture", "camera equipment", "pet supplies", "books", "gourmet food items", "fashion accessories", "DIY tools", "art supplies",
                    "baby products", "musical instruments", "sporting goods", "car accessories", "gardening tools", "cooking utensils", "party supplies",
                    "samsung s20 ultra", 'IQOO Z6 lite','realme 9','realme 8i','xiaomi','redmi','poco','pocox2','Noise fit']
    res = create_examples( queries,tokens,'Product Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    queries = ["#tkn# under #price#","Show me #tkn# in the range of #price#","#tkn# about the price of #price#"]
    r = []
    for q in queries:
        for p in ["1000","100000","23000","549","999","23000","4320"]:
            r.append(q.replace("#price#",p))
    queries = r
    tokens = ["mobiles","laptops","shoes","groceries","diamonds","electronics","gifts","notebooks","ipad","iphone"]
    res = create_examples( queries,tokens,'Product Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    return dataset[0], dataset[1]