import csv, random
from protocol_activator import protocol_map_str

def get_dataset(split = 0.9, limit =  None):
    """
    Generates the dataset
    """
    dataset = []
    # Open dataset.csv and get it's contents
    with open('Datasets/MusicPlayer/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = list(reader)[:limit] if limit else list(reader)

    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())

    split_idx = int(split*len(dataset))
    random.shuffle(dataset)
    return dataset[:split_idx], dataset[split_idx:]

def generate_data(search_keys, search_prompts):
    dataset = []
    for k in search_keys:
        for p in search_prompts:
            dataset.append([p+" "+k,f"<INTENT> {protocol_map_str['MusicPlayerProtocol']} 1 </INTENT> <PARAMS> search_value = {k} </PARAMS> <TEXT> Playing the song of {k} online </TEXT>", f'MusicPlayerProtocol'])
    return dataset

def getSyntheticData():
    dataset = []
    # Play Song by artist
    artists = ["Arijit Singh", "Taylor Swift", "Ed Sheeran", "Lata Mangeshkar", "Rihanna", "Beyoncé", "Ariana Grande", "Kishore Kumar", 
                 "Justin Bieber", "Neha Kakkar", "Bruno Mars", "Adele", "Sonu Nigam", "Billie Eilish", "Atif Aslam", "Lady Gaga", 
                 "Selena Gomez", "Shreya Ghoshal", "Coldplay", "Katy Perry", "Mohd. Rafi", "Eminem", "BTS", "Drake", "Yo Yo Honey Singh", 
                 "Udit Narayan", "Michael Jackson", "Neha Kakkar", "Shawn Mendes", "A.R. Rahman", "Camila Cabello", "Amaal Mallik", 
                 "Maroon 5", "Tony Kakkar", "Nicki Minaj", "Badshah", "Zayn Malik", "Alan Walker", "Jubin Nautiyal", "Imagine Dragons", 
                 "Alisha Chinai", "The Weeknd", "Jagjit Singh", "Sia", "Mika Singh", "Charlie Puth", "Diljit Dosanjh", "Sam Smith", 
                 "Vishal Dadlani", "Marshmello", "Ankit Tiwari", "Queen", "Lucky Ali", "Halsey", "Hardy Sandhu", "John Legend", 
                 "Kailash Kher", "Demi Lovato", "Raftaar", "Twenty One Pilots"]
    prompts = [
        "Can you play a song of", "Why don't you play songs of", "I'd like to listen to a song by",
        "Could you please play something from", "How about playing a track from", "I'm in the mood for some music by",
        "Play a song by", "Let's listen to something by", "Can you put on a song from", "I want to hear a track by",
        "Play some tunes from", "Could you play something by", "I'm craving some music from", "Why not play songs from",
        "I'm feeling like listening to", "How about a song from", "Please play a track by", "Put on a song by",
        "Let's hear something from", "Can you play a tune from", "I'd love to hear a song by", "Why don't we listen to",
        "Play a track from", "Let's enjoy some music by", "How about some tunes from", "Can you play something by",
        "I'm in the mood for a song by", "Play a track by", "Could you put on some music by", "I'd like to hear something from"
    ]
    dataset.extend(generate_data(artists,prompts))

    # Play Song by album
    albums = [
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
    prompts = [
        "Can you play songs from",
        "I'm craving some songs from", "How about playing some tunes from", "Let's listen to some songs from",
        "Play some tracks from", "Can we hear some music from", "I'd love to listen to some tracks from",
        "How about some tunes from", "I'm in the mood for some songs from", "Play some songs from",
        "Can you put on some tunes from", "Let's hear some music from", "How about some songs from",
        "I'm feeling like listening to some tracks from", "Play some tracks from", "Could you play some songs from",
        "Let's put on some music from", "How about playing some songs from", "Can you play some tracks from",
        "I'd like to hear some songs from", "Let's play some music from", "How about listening to some songs from",
        "I'm in the mood for some tunes from", "Could you put on some tracks from", "Let's enjoy some songs from",
        "Play some tunes from", "Can you play some music from", "Let's listen to some tunes from",
        "I'd love to hear some music from", "How about some music from", "I'm in the mood for some albums from",
        "Play some albums from", "Can you put on some albums from", "Let's hear some albums from",
        "How about playing some albums from", "I'd like to hear some albums from", "Play some tracks from",
        "Can you play some albums from", "Let's enjoy some albums from", "How about some albums from",
        "I'm feeling like listening to some albums from", "Play some albums from", "Could you play some albums from",
        "Let's put on some albums from"
    ]
    dataset.extend(generate_data(albums,prompts))


    # Play Song by Song name
    songs = [
        "Shape of You", "Roar", "Despacito", "Bohemian Rhapsody", "Someone Like You",
        "Believer", "Girls Like You", "Uptown Funk", "Hips Don't Lie", "See You Again",
        "Senorita", "Channa Mereya", "Old Town Road", "Perfect", "Tum Hi Ho",
        "Shallow", "Baby", "Cheap Thrills", "Closer", "I Will Always Love You",
        "Tere Bina", "Ae Dil Hai Mushkil", "Muskurane Ki Wajah", "Dil Diyan Gallan",
        "Teri Meri", "Gerua", "Tum Hi Ho Bandhu", "Galliyan", "Zara Zara",
        "Tum Se Hi", "Chaiyya Chaiyya", "Peaky blinders", "Billonera", "legends never die",
        "Alone pt II", "Faded", 
    ]
    prompts_= [
        "How about playing", "Can you play", "Let's listen to", "I'd like to hear",
        "Play", "Put on", "Could you play", "Why not try", "I'm in the mood for",
        "How about some", "Play some", "Let's enjoy", "I'm craving", "Can we hear",
        "I'd love to listen to", "Why not play", "How about listening to", "Play some tunes from",
        "Let's hear", "I'm feeling like listening to"
    ]
    dataset.extend(generate_data(songs,prompts))

    return dataset