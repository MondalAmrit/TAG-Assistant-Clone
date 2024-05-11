from Intents.Music.actions import play_song
from Intents.Internet.actions import *
from Intents.Weather.actions import *
def executor(intent):
    print('Intent called for', intent)
    if intent == 'Music':
        play_song(None)
    elif intent == 'Image Search':
        get_image('AI images')
    elif intent == 'Current Weather Forecast':
        return str(get_forecast('New Delhi')['current'])
    elif intent == 'Future Weather Forecast':
        return str(get_future_forecast('New Delhi','2024-05-13'))
    return None

