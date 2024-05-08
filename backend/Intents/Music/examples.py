import csv, random
# from protocol_activator import protocol_map_str

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
    # Songs by Artists
    queries = ["Can you play a song of #tkn#", "Why don't you play songs of #tkn#", "I'd like to listen to a song by #tkn#",
        "Could you please play something from #tkn#", "How about playing a track from #tkn#", "I'm in the mood for some music by #tkn#",
        "Play a song by #tkn#", "Let's listen to something by #tkn#", "Can you put on a song from #tkn#", "I want to hear a track by #tkn#",
        "Play some tunes from #tkn#", "Could you play something by #tkn#", "I'm craving some music from #tkn#", "Why not play songs from #tkn#",
        "I'm feeling like listening to #tkn#", "How about a song from #tkn#", "Please play a track by #tkn#", "Put on a song by #tkn#",
        "Let's hear something from #tkn#", "Can you play a tune from #tkn#", "I'd love to hear a song by #tkn#", "Why don't we listen to #tkn#",
        "Play a track from #tkn#", "Let's enjoy some music by #tkn#", "How about some tunes from #tkn#", "Can you play something by #tkn#",
        "I'm in the mood for a song by #tkn#", "Play a track by #tkn#", "Could you put on some music by #tkn#", "I'd like to hear something from #tkn#",
        "I think it's better to play #tkn#'s songs", "I want you to play #tkn# songs"]
    tokens = ["Arijit Singh", "Taylor Swift", "Ed Sheeran", "Lata Mangeshkar", "Rihanna", "Beyoncé", "Ariana Grande", "Kishore Kumar", 
                 "Justin Bieber", "Neha Kakkar", "Bruno Mars", "Adele", "Sonu Nigam", "Billie Eilish", "Atif Aslam", "Lady Gaga", 
                 "Selena Gomez", "Shreya Ghoshal", "Coldplay", "Katy Perry", "Mohd. Rafi", "Eminem", "BTS", "Drake", "Yo Yo Honey Singh", 
                 "Udit Narayan", "Michael Jackson", "Neha Kakkar", "Shawn Mendes", "A.R. Rahman", "Camila Cabello", "Amaal Mallik", 
                 "Maroon 5", "Tony Kakkar", "Nicki Minaj", "Badshah", "Zayn Malik", "Alan Walker", "Jubin Nautiyal", "Imagine Dragons", 
                 "Alisha Chinai", "The Weeknd", "Jagjit Singh", "Sia", "Mika Singh", "Charlie Puth", "Diljit Dosanjh", "Sam Smith", 
                 "Vishal Dadlani", "Marshmello", "Ankit Tiwari", "Queen", "Lucky Ali", "Halsey", "Hardy Sandhu", "John Legend", 
                 "Kailash Kher", "Demi Lovato", "Raftaar", "Twenty One Pilots"]
    res = create_examples( queries,tokens,'Music',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Songs by Albums
    tokens = [
        "Jab Tak Hai Jaan by A.R. Rahman", "Kal Ho Naa Ho by Shankar-Ehsaan-Loy",
        "Aashiqui 2 by Mithoon", "Dil Se.. by A.R. Rahman",
        "Rang De Basanti by A.R. Rahman", "Rockstar by A.R. Rahman",
        "Lagaan by A.R. Rahman", "Dilwale Dulhania Le Jayenge by Jatin-Lalit",
        "Kabhi Khushi Kabhie Gham by Jatin-Lalit", "Mohabbatein by Jatin-Lalit",
        "Kuch Kuch Hota Hai by Jatin-Lalit", "Dhadak by Ajay-Atul",
        "Gully Boy by Various Artists", "Student of the Year by Vishal-Shekhar",
        "Kabir Singh by Various Artists", "Ek Villain by Ankit Tiwari",
        "Jai Ho by Sajid-Wajid", "Barfi! by Pritam", "Raanjhanaa by A.R. Rahman",
        "Yeh Jawaani Hai Deewani by Pritam","1989 by Taylor Swift", "21 by Adele", "Lemonade by Beyoncé",
        "Recovery by Eminem", "My World by Justin Bieber", "X by Ed Sheeran",
        "Dangerous Woman by Ariana Grande", "21 by Sonu Nigam",
        "The Fame by Lady Gaga", "Fearless by Taylor Swift"
    ]
    queries = [
        "Can you play songs from #tkn#",
        "I'm craving some songs from #tkn#", "How about playing some tunes from #tkn#", "Let's listen to some songs from #tkn#",
        "Play some tracks from #tkn#", "Can we hear some music from #tkn#", "I'd love to listen to some tracks from #tkn#",
        "How about some tunes from #tkn#", "I'm in the mood for some songs from #tkn#", "Play some songs from #tkn#",
        "Can you put on some tunes from #tkn#", "Let's hear some music from #tkn#", "How about some songs from #tkn#",
        "I'm feeling like listening to some tracks from #tkn#", "Play some tracks from #tkn#", "Could you play some songs from #tkn#",
        "Let's put on some music from #tkn#", "How about playing some songs from #tkn#", "Can you play some tracks from #tkn#",
        "I'd like to hear some songs from #tkn#", "Let's play some music from #tkn#", "How about listening to some songs from #tkn#",
        "I'm in the mood for some tunes from #tkn#", "Could you put on some tracks from #tkn#", "Let's enjoy some songs from #tkn#",
        "Play some tunes from #tkn#", "Can you play some music from #tkn#", "Let's listen to some tunes from #tkn#",
        "I'd love to hear some music from #tkn#", "How about some music from #tkn#", "I'm in the mood for some albums from #tkn#",
        "Play some albums from #tkn#", "Can you put on some albums from #tkn#", "Let's hear some albums from #tkn#",
        "How about playing some albums from #tkn#", "I'd like to hear some albums from #tkn#", "Play some tracks from #tkn#",
        "Can you play some albums from #tkn#", "Let's enjoy some albums from #tkn#", "How about some albums from #tkn#",
        "I'm feeling like listening to some albums from #tkn#", "Play some albums from #tkn#", "Could you play some albums from #tkn#",
        "Let's put on some albums from #tkn#", "Play #tkn# songs", "I want you to play the ablum #tkn# songs"
    ]
    res = create_examples( queries,tokens,'Music',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

     # Play Song by Song name
    tokens = [
        "Shape of You", "Roar", "Despacito", "Bohemian Rhapsody", "Someone Like You",
        "Believer", "Girls Like You", "Uptown Funk", "Hips Don't Lie", "See You Again",
        "Senorita", "Channa Mereya", "Old Town Road", "Perfect", "Tum Hi Ho",
        "Shallow", "Baby", "Cheap Thrills", "Closer", "I Will Always Love You",
        "Tere Bina", "Ae Dil Hai Mushkil", "Muskurane Ki Wajah", "Dil Diyan Gallan",
        "Teri Meri", "Gerua", "Tum Hi Ho Bandhu", "Galliyan", "Zara Zara",
        "Tum Se Hi", "Chaiyya Chaiyya", "Peaky blinders", "Billonera", "legends never die",
        "Alone pt II", "Faded", 
    ]
    queries = [
        "How about playing #tkn#", "Can you play #tkn#", "Let's listen to #tkn#", "I'd like to hear #tkn#",
        "Play #tkn#", "Put on #tkn#", "Could you play #tkn#", "Why not try #tkn#", "I'm in the mood for #tkn#",
        "How about some #tkn#", "Play some #tkn#", "Let's enjoy #tkn#", "I'm craving #tkn#", "Can we hear #tkn#",
        "I'd love to listen to #tkn#", "Why not play #tkn#", "How about listening to #tkn#", "Play some tunes from #tkn#",
        "Let's hear #tkn#", "I'm feeling like listening to #tkn#", "play #tkn# song", "start music with #tkn# song",
    ]
    res = create_examples( queries,tokens,'Music',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]