import csv


def get_dataset(limit=None):
    """
    Generates the dataset
    """
    dataset = []
    # Open dataset.csv and get its contents
    with open('Datasets/YouTubeSearch/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = list(reader)[:limit] if limit else list(reader)

    dataset = [[i[0], "<QUERY>" + i[1] + "</QUERY>"] for i in dataset]

    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())
    return dataset


def generate_data(prompts, responses):
    dataset = []
    for prompt in prompts:
        for response in responses:
            dataset.append([prompt, "<RESULT>" + response + "</RESULT>"])
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
    results = ["Here's a video tutorial on how to tie a tie: https://www.youtube.com/watch?v=HXJx8j7JpKY",
               "Prepare to laugh with these hilarious cat videos: https://www.youtube.com/watch?v=VO0RqUFeMOM",
               "Start your day right with these healthy breakfast recipes: https://www.youtube.com/watch?v=t4t1Vj5-NLQ",
               "Embark on a virtual journey with these exciting travel vlogs: https://www.youtube.com/watch?v=hROKtPqktO8",
               "Spruce up your living space with these creative DIY home decor ideas: https://www.youtube.com/watch?v=GHrJbIP7DsY",
               "Catch up on the latest movie trailers here: https://www.youtube.com/watch?v=xy8aJw1vYHo",
               "Get fit and stay healthy with these effective workout routines: https://www.youtube.com/watch?v=04kAfDdqEfg",
               "Get inspired to bake with these stunning cake decorating ideas: https://www.youtube.com/watch?v=7h6Vjd8z_7E", 
               "Improve your photography skills with these useful tips: https://www.youtube.com/watch?v=hVuTuib65WM",
               "Understand the basics of artificial intelligence with this comprehensive explanation: https://www.youtube.com/watch?v=ad79nYk2keg",
               "Stay stylish with the latest fashion trends: https://www.youtube.com/watch?v=IHeST5I_vLU",
               "Travel on a budget with these practical tips: https://www.youtube.com/watch?v=Puho7BrsTqE",
               "Master the kitchen with this beginner's cooking guide: https://www.youtube.com/watch?v=bsYzWK3cxOM",
               "Tips to learn a new language: https://www.youtube.com/watch?v=o_XVt5rdpFY",
               "Stay fit at home with these workout routines that require no equipment: https://www.youtube.com/watch?v=cbKkB3POqaY",
               "Boost your productivity with these effective hacks: https://www.youtube.com/watch?v=5Fg7Hcse1QY",
               "Understand the fundamentals of music theory with this introductory lesson: https://www.youtube.com/watch?v=oU4i59Mf8Yo",
               "Stay updated on the latest tech with these insightful reviews: https://www.youtube.com/watch?v=0O2yTG3n1Vc",
               "Grow your own garden with these helpful tips: https://www.youtube.com/watch?v=yvVft_ZofK8"
               ]

    dataset.extend(generate_data(queries, results))

    # Creators
    queries = ["PewDiePie", "T-Series", "MrBeast", "Dude Perfect", "5-Minute Crafts", "Markiplier", "Jenna Marbles",
               "Smosh", "Rhett & Link", "Ryan's World", "Good Mythical Morning", "Jake Paul", "Ninja", "James Charles",
               "David Dobrik", "Liza Koshy", "Casey Neistat", "Emma Chamberlain", "Lilly Singh", "The Try Guys"]
    results = ["Here's a video of PewDiePie : https://www.youtube.com/watch?v=ahx0iw78lUE", 
               "Here's a video of T-Series : https://www.youtube.com/watch?v=qG89dlH0icI", 
               "Here's a video of MrBeast : https://www.youtube.com/watch?v=erLbbextvlY ", 
               "Here's a video of Dude Perfect : https://www.youtube.com/watch?v=tnb8XcGbYCM", 
               "Here's a video of 5-Minute Crafts : https://www.youtube.com/watch?v=QTzTOTSnrNg", 
               "Here's a video of Markiplier : https://www.youtube.com/watch?v=aA0LiGAulOc", 
               "Here's a video of Jenna Marbles: https://www.youtube.com/watch?v=KHCfr7qvkJs", 
               "Here's a video of Smosh : https://www.youtube.com/watch?v=QedF7G8ut_k", 
               "Here's a video of Rhett & Link : https://www.youtube.com/watch?v=eEb9niZF-ik", 
               "Here's a video of Ryan's World : https://www.youtube.com/watch?v=Luc7qLaMzRc",
               "Here's a video of Good Mythical Morning : https://www.youtube.com/watch?v=hjrHtfdBpU8", 
               "Here's a video of Jake Paul : https://www.youtube.com/watch?v=WKx1LebwBLs", 
               "Here's a video of Ninja : https://www.youtube.com/watch?v=RX02QECyJO0", 
               "Here's a video of James Charles : https://www.youtube.com/watch?v=e46rvfVSFeg", 
               "Here's a video of David Dobrik : https://www.youtube.com/watch?v=-b1WnjKvcUg",
               "Here's a video of Liza Koshy :https://www.youtube.com/watch?v=GyveeERbia4",
               "Here's a video of Casey Neistat :https://www.youtube.com/watch?v=h-vWRLGnTGg",
               "Here's a video of Emma Chamberlain :https://www.youtube.com/watch?v=7Z0fToNvwy4",
               "Here's a video of Lilly Singh :https://www.youtube.com/watch?v=hZULVP4f5F4",
               "Here's a video of The Try Guys :https://www.youtube.com/watch?v=npAypF3RXIs"]
    


    # Out of Order
    prompts = [
        "I don't understand.", "That's not what I searched for.", "Could you please provide better results?",
        "This isn't relevant to my query.", "I'm not sure what you're showing me.", "I need more accurate results.",
        "Let's try a different search.", "Could you please refine the search?", "This doesn't match my expectations.",
        "I'm having trouble finding what I'm looking for."
    ]
    responses = [
        "I'm sorry, I'll try to improve the search results.", "Let me refine the search criteria.",
        "I'll find better results for you.", "Apologies for the inconvenience, I'll adjust the search.",
        "I'll make sure to provide more relevant results next time.", "Let's try another search query.",
        "I'll work on getting more accurate results for you.", "I appreciate your feedback, I'll refine the search.",
        "I understand, I'll find what you're looking for.", "I'll make the necessary adjustments to the search."
    ]
    dataset.extend(generate_data(prompts, responses))

    return dataset
