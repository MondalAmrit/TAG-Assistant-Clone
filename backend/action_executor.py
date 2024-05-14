from Intents.Music.actions import play_song
from Intents.Internet.actions import *
from Intents.Weather.actions import *
from Intents.YouTube.actions import *
def executor(intent, args = ''):
    print('Intent called for', intent)
    if intent == 'Music':
        play_song(args)
    elif intent == 'Image Search':
        get_image(args)
    elif intent == 'Open Website':
        open_url(args)
    elif intent == 'Product Search':
        get_product(args)
    elif intent == 'Information':
        get_info(args)
    elif intent == 'Location':
        get_coords(args)
    elif intent == 'YouTube Search':
        YT_search(args)
    elif intent == 'Current Weather Forecast':
        return str(get_forecast(args)['current'])
    # elif intent == 'Future Weather Forecast':
    #     return str(get_future_forecast(args,'2024-05-16'))
    return None

