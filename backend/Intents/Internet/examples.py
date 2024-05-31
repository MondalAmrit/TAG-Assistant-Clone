import csv, re, random
# from protocol_activator import protocol_map_str

IntentName = "Internet"
ActionMap = ["Information","Open Website","Image Search","Product Search",]

def generate_dataset(split = 0.9):
    """ Generates the dataset """
    # Open dataset.csv and get it's contents (Not done yet)
    
    # Add Synthetic data generation
    return synthetic_examples_dataset(split = split)

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

def synthetic_examples_dataset(split = 0.9):
    """ Write down you synthetic examples here """
    dataset = [[],[]]
    # information
    queries = ["Find information about {Query}","Tell me about {Query}","Provide details about {Query}",
                    "Explain the concept of {Query}","What is the history of {Query}","Provide information about {Query}",
                    "Could you enlighten me on {Query}","I'm curious about {Query}","Can you shed some light on {Query}",
                    "Give me insights into {Query}","I'd like to explore {Query}","Help me understand {Query}",
                    "I'm interested in learning about {Query}","Share some knowledge about {Query}","Can you delve into {Query}",
                    "Clarify the significance of {Query}","I want to know more about {Query}","Unravel the mysteries of {Query}",
                    "Educate me on {Query}","Could you elucidate {Query}","Brief me on {Query}","Give me an overview of {Query}",
                    "I'm eager to discover {Query}","Could you provide some background on {Query}","Let's delve into the details of {Query}",
                    "Enlighten me about {Query}","Elaborate on {Query}",
                "Internet Search for {Query}", "Search online for {Query}", "Search in chrome for {Query}",
                "Search on bing for {Query}", "search on edge for {Query}", "Why don't you search for {Query} in the internet?",
                "Why don't you search {Query} in chrome", "{Query} in internet"]
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
    r = [{"Query":i} for i in tokens]
    res = create_examples( queries,r,'Information',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    
    # open urls
    queries = ['open {Query}', 'can you please open {Query}', 'I think its better to open {Query}', "why don't you open {Query}", 'please open {Query}', 'Just open {Query}',
                'Navigate to {Query}', 'Launch {Query}', 'Go to {Query}', 'Visit {Query}', 'Access {Query}', 'Take me to {Query}', 
                'Direct me to {Query}', 'Load {Query}', 'Explore {Query}', 'Check out {Query}', 'I want you to open {Query}', "Why don't you open {Query}?",
                "show me the {Query}", "I want you to open {Query}", "Hey, Why don't you open {Query} ?", "Just open the {Query}",
                "Open {Query} in a browser", "Quickly open the {Query}"]
    tokens = ['leetcode', 'linkedin', 'amazon', 'github', 'google', 'gmail', 'geeksforgeeks', 'stackoverflow', 'netflix', 'codechef',
                'youtube', 'facebook', 'twitter', 'instagram', 'wikipedia', 'reddit', 'quora', 'ebay', 'microsoft', 'apple',
                'spotify', 'bbc', 'cnn', 'nytimes', 'yahoo', 'bing', 'wordpress', 'pinterest', 'dropbox', 'twitch']
    r = [{"Query":i} for i in tokens]
    res = create_examples( queries,r,'Open Website',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Image Search
    queries = ["Give me an image of a {Query}", "Image of a {Query}", "Show me pictures of {Query}", "Find me an image of a tropical {Query}", "I need a picture of a mountain {Query}", 
               "Can you provide an image of a {Query}", "I'm looking for pictures of {Query}", "Image search: {Query}", "Please show me photos of {Query}", 
               "Find an image related to {Query}", "search this image {Query}", "Why don't you search for this image {Query} on google?",
               "search this photo {Query} on google", "search for image of {Query} online", "images of ", "I need images for ", "related images for ",
               "Give me the images of {Query}", "get the image results for {Query}","{Query} images"]
    tokens = ["cat", "sunset", "dogs", "tropical beach", "mountain landscape", "happy family", "famous landmarks", "beautiful flowers", "city skylines", "technology",
                  "human","rats","college","metro","flights","auto",'cab','car','comb','cost','country','currency','note','book']
    r = [{"Query":i} for i in tokens]
    res = create_examples( queries,r,'Image Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # product
    queries = ["Show me {Query}","Show me the products related to {Query}" , "Tell me about {Query}", "Can you provide details {Query}", "Give me information about {Query}", "Provide information about {Query}", "Give me details about {Query}", "Show me available {Query}",
                    "What are the options for {Query}", "I'm interested in {Query}", "Please display {Query}", "Could you show me {Query}", "I'd like to see {Query}", "I'm looking for details on {Query}",
                    "Please provide info on {Query}", "Can you show me {Query}", "What's available for {Query}", "Related products for {Query}",
                    "Product options for {Query}",'Amazon search for {Query}', "search for the {Query} online", "get me the {Query} products",
                    "Why don't you get me the product related to {Query}", "Show me the prices for the {Query}",
                    "latest {Query}","{Query} new models","brand new {Query}"]

    tokens = ["smartphones on the market", "designer handbags", "laptops", "sports shoes", "kitchen appliances", "luxury watches", "home decor items",
                    "gaming consoles", "fitness trackers", "skincare products", "smart home devices", "office chairs", "travel accessories", "headphones",
                    "outdoor furniture", "camera equipment", "pet supplies", "books", "gourmet food items", "fashion accessories", "DIY tools", "art supplies",
                    "baby products", "musical instruments", "sporting goods", "car accessories", "gardening tools", "cooking utensils", "party supplies",
                    "samsung s20 ultra", 'IQOO Z6 lite','realme 9','realme 8i','xiaomi','redmi','poco','pocox2','Noise fit']
    r = [{"Query":i} for i in tokens]
    res = create_examples( queries,r,'Product Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    queries = ["{Query} under {Quantity}","Show me {Query} in the range of {Quantity}","{Query} about the price of {Quantity}"]
    tokens = ["mobiles","laptops","shoes","groceries","diamonds","electronics","gifts","notebooks","ipad","iphone"]
    r = []
    for t in tokens:
        for p in ["1000","100000","23000","549","999","23000","4320"]:
            r.append({"Query":t,"Price":p})
    res = create_examples( queries,r,'Product Search',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    return dataset[0], dataset[1]