songs_data = {
    'song1': {
        'artist': 'Artist1',
        'song_name': 'Song1',
        'mood': 'Happy',
        'state': 'CA',
        'movie': 'Movie1',
        'actor': 'Actor1'
    },
    'song2': {
        'artist': 'Artist2',
        'song_name': 'Song2',
        'mood': 'Sad',
        'state': 'NY',
        'movie': 'Movie2',
        'actor': 'Actor2'
    },
    # Add more songs as needed
}


def get_song_list(search_type,search_value):
    results = []
    for song, details in songs_data.items():
        if details[search_type].lower() == search_value.lower():
            results.append(song)
    return results

def play_song(query):
    print(" this function is currently unavailable")
    return None


def create_playList(query):
    print(" this function is currently unavailable")
    return None

functionMap = {
    1: get_song_list,
    2: play_song,
    3: create_playList
}

print(get_song_list("artist","Artist2"))