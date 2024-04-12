import csv
def get_dataset(limit =  None):
    """
    Generates the dataset
    """
    dataset = []
    # Open dataset.csv and get it's contents
    with open('Datasets/BasicChat/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = list(reader)[:limit] if limit else list(reader)

    dataset = [[i[0],"<TEXT>" + i[1] + "</TEXT>"] for i in dataset]

    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())
    return dataset

def generate_data(prompts, responses):
    dataset = []
    for prompt in prompts:  
        for response in responses:  
            dataset.append([prompt, "<TEXT>" + response + "</TEXT>"])
    return dataset    

def getSyntheticData():
    """
    Generates the Synthetic dataset
    """
    dataset = []

    # Greetings
    prompts = ["Hello", "Hi", "Hey", "Good day", "Greetings", "Howdy", "Salutations", "Yo", "What's up", "Bonjour"]
    responses = ["Hello! How can I help you today?", "Hi there! What would you like to talk about?",
                        "Hey! How may I assist you?", "Good day! How can I help you today?", 
                        "Greetings! What would you like to talk about?", "Howdy! How can I assist you?", 
                        "Salutations! What can I do for you?", "Yo! How may I assist you?", 
                        "What's up! How can I help you today?", "Hey! Nice to see you. How can I assist you?"]
    dataset.extend(generate_data(prompts,responses))
    prompts = ["Welcome", "Good to see you", "Nice to meet you", "Pleasure to meet you", "How are you?", "What's new?", "How's it going?", "Long time no see", "How have you been?", "How's everything?"]
    responses = ["Welcome! How can I assist you today?", "Good to see you! What can I do for you?",
                        "Nice to meet you! What would you like to talk about?", "Pleasure to meet you! How may I assist you?", 
                        "I'm doing well, thank you! How about you?", "Not much, just here to help. What can I do for you?",
                        "It's going great! How can I assist you?", "Long time no see! What brings you here today?", 
                        "I've been good, thank you for asking. How can I help you?", "Everything's good here! How about you?"]
    dataset.extend(generate_data(prompts, responses))
    
    # Self
    prompts = ["What's your name?", "Who are you?", "Tell me about yourself", "What is TAG?", "What can you do?"]
    responses = ["I'm TAG (Task Automation via GPT), a GPT-based chatbot designed to assist with various tasks.",
             "I'm TAG, a chatbot powered by GPT-based BERT Tokenized Text to Text Generation.",
             "I am TAG, an AI chatbot designed to help users leverage the power of automation through GPT-based text generation.",
             "TAG stands for Task Automation via GPT. It is a chatbot powered by GPT-based BERT Tokenized Text to Text Generation.",
             "TAG is designed to help users achieve the power of AI on low-level devices and leverage the power of automation through GPT-based text generation."]
    dataset.extend(generate_data(prompts,responses))
    prompts = ["How are you generating text?", "What technology do you use?", "Can you explain your text generation process?"]
    responses = ["I generate text using GPT-based BERT Tokenized Text to Text Generation.",
                "My text generation process is based on GPT architecture with BERT tokenization.",
                "I utilize GPT-based algorithms to generate text responses."]
    dataset.extend(generate_data(prompts,responses))
    prompts = ["How can you add value to me?", "What benefits do you offer?", "Why should I use your services?"]
    responses = ["I can help you automate tasks and leverage the power of AI on low-level devices.",
                "By using my services, you can streamline processes and save time through automation.",
                "I offer the ability to access AI capabilities for task automation and enhanced efficiency."]
    dataset.extend(generate_data(prompts,responses))
    prompts = ["What tasks can you assist with?", "Can you provide examples of what you can do?", "What are your capabilities?"]
    responses = ["I can assist with a wide range of tasks, including text generation, language understanding, and task automation.",
                "Examples of tasks I can help with include answering questions, summarizing text, and generating creative content.",
                "My capabilities include natural language processing, task automation, and providing contextual responses."]
    dataset.extend(generate_data(prompts,responses))
    prompts = ["Can I customize your behavior?", "Are there any settings I can adjust?", "Do you offer any personalization options?"]
    responses = ["Currently, I do not offer customization options, but I can adapt to your preferences over time.",
                "At the moment, my behavior is not customizable, but I aim to provide personalized experiences in the future.",
                "I do not have specific settings or personalization options, but I strive to understand and adapt to your needs."]
    dataset.extend(generate_data(prompts,responses))

    # Common Sense
    jokes_prompts = ["Tell me a joke.", "Can you make me laugh?", "Do you have any funny stories?",
                 "I could use a laugh. Got any jokes?", "What's the funniest thing you know?",
                 "Got any good jokes for me?", "In the mood for some humor. Hit me with a joke!",
                 "I need a pick-me-up. Tell me a joke.", "Feeling down. Maybe a joke will cheer me up?",
                 "Can you lighten the mood with a joke?"]
    jokes_responses = ["Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
                    "Why was the math book sad? Because it had too many problems.",
                    "What do you call fake spaghetti? An impasta!",
                    "Why don't skeletons fight each other? They don't have the guts.",
                    "Why couldn't the bicycle stand up by itself? It was two-tired.",
                    "What did one hat say to the other? You stay here, I'll go on ahead.",
                    "Why don't eggs tell jokes? Because they might crack up!",
                    "How does a penguin build its house? Igloos it together.",
                    "Why did the scarecrow win an award? Because he was outstanding in his field.",
                    "Why don't scientists trust stairs? Because they're always up to something."]
    facts_prompts = ["Tell me an interesting fact.", "Can you share some trivia?", "Give me a random fact.",
                    "I love learning new things. Got any facts for me?", "What's the most interesting fact you know?",
                    "Looking for something fascinating. Any facts?", "Tell me something I didn't know.",
                    "I'm curious. Share a fact with me.", "Hit me with some knowledge. What's a cool fact?",
                    "I'm bored. Entertain me with an interesting fact."]
    facts_responses = ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
                    "The shortest war in history lasted only 38 minutes. It was between Britain and Zanzibar in 1896.",
                    "The unicorn is the national animal of Scotland.",
                    "Octopuses have three hearts.",
                    "The world's oldest piece of chewing gum is over 9,000 years old!",
                    "A group of flamingos is called a flamboyance.",
                    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
                    "Peanuts are not nuts. They are legumes.",
                    "The average person will spend six months of their life waiting for red lights to turn green.",
                    "The shortest war in history was between Zanzibar and England in 1896. Zanzibar surrendered after 38 minutes."]
    events_prompts = ["What's happening in the world?", "Any recent events?", "Can you tell me about any upcoming events?",
                    "I'm out of the loop. Anything noteworthy going on?", "What's the latest news?",
                    "Is there anything exciting happening?", "Any big events on the horizon?",
                    "What's the buzz lately?", "I'm curious about current events. Fill me in.",
                    "Tell me about any interesting events."]
    events_responses = ["Recently, NASA's Perseverance rover successfully landed on Mars, marking an important milestone in space exploration.",
                        "The Olympics are scheduled to take place in Paris in 2024, bringing together athletes from around the world to compete in various sports.",
                        "Tomorrow is Earth Day, a day dedicated to raising awareness about environmental issues and promoting conservation efforts.",
                        "The Cannes Film Festival is set to take place next month, showcasing the latest films from around the world.",
                        "The G20 Summit is happening next week, where leaders from the world's largest economies will meet to discuss global issues.",
                        "A total solar eclipse will occur next month, visible from parts of South America and Antarctica.",
                        "The Met Gala, one of the most anticipated events in the fashion industry, is happening next week in New York City.",
                        "The World Cup qualifiers are underway, with teams competing for a spot in the upcoming tournament.",
                        "The Nobel Prizes will be awarded next month, recognizing individuals and organizations for their outstanding contributions.",
                        "A major climate conference is scheduled for next year, where world leaders will discuss strategies to combat climate change."]
    trends_prompts = ["What's trending right now?", "Any popular topics?", "Can you tell me about current trends?",
                    "I'm interested in what's popular. What's trending?", "What are people talking about these days?",
                    "I want to stay up-to-date. Fill me in on the latest trends.",
                    "Is there anything everyone is talking about lately?", "I'm curious about current trends. What's hot right now?",
                    "Tell me about any recent trends.", "I'm looking for something new. What's trending?"]
    trends_responses = ["The latest trend on social media is the 'What I Eat in a Day' challenge, where users share videos of their daily meals.",
                        "Virtual reality gaming is becoming increasingly popular, with more people investing in VR headsets and immersive gaming experiences.",
                        "Sustainability and eco-friendly living are emerging as major trends, with consumers seeking products and services that minimize environmental impact.",
                        "Remote work is a growing trend, with many companies adopting flexible work arrangements and digital nomadism on the rise.",
                        "NFTs (Non-Fungible Tokens) are gaining popularity in the art world, with digital artworks selling for millions of dollars.",
                        "Plant-based diets and veganism are on the rise, driven by concerns about health, animal welfare, and the environment.",
                        "Cryptocurrency and blockchain technology are trending, with Bitcoin and other digital currencies making headlines.",
                        "Minimalism and decluttering are trending lifestyle choices, with people embracing simplicity and mindful consumption.",
                        "DIY home improvement projects are trending, as people spend more time at home and look for ways to enhance their living spaces.",
                        "Mindfulness and meditation practices are gaining popularity, with apps and online resources offering guidance and support."]
    all_prompts = jokes_prompts + facts_prompts + events_prompts + trends_prompts
    all_responses = jokes_responses + facts_responses + events_responses + trends_responses
    dataset.extend(generate_data(all_prompts, all_responses))

    # Out of Order
    prompts = [
        "I don't understand.","That's not relevant to our conversation.","Could you please provide more context?",
        "I'm not sure what you're referring to.","I'm sorry, I don't follow.","I'm not sure how to respond to that.",
        "Let's get back on topic.","Could you please rephrase your question?","That seems unrelated to our discussion.",
        "I'm having trouble understanding your message."
    ]
    responses = [
        "I'm sorry, I'm not sure how to help with that.","That doesn't seem relevant to our conversation.",
        "I'm not sure what you're asking. Can you clarify?","I'm afraid I can't assist with that.",
        "Let's focus on the topic at hand.","I'm sorry, I can't provide a response to that.",
        "Perhaps we should return to our original topic.","I'm having difficulty understanding. Could you provide more information?",
        "I'm sorry, I'm not programmed to handle that request.","Let's try to stay on track with our conversation."
    ]
    dataset.extend(generate_data(prompts, responses))
    
    return dataset