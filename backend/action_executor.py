from Intents.Music.actions import play_song
from Intents.Internet.actions import *
from Intents.Weather.actions import *
from Intents.YouTube.actions import *
from Intents.System.actions import *
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
    elif intent == 'Volume':
        return 'The volume is now at ' + setVolume(int(args) if args != '' else None)
    elif intent == 'Brightness':
        return 'The Brightness is now at ' + str(setBrightness(int(args) if args != '' else None))
    elif intent in ('Datetime','Current Date','Year','TimeStamp','Time Zone','Current Time'):
        return 'The current date time is ' + str(getCurrDateTime())
    elif intent == 'Battery':
        return 'The Battery Status is ' + str(batteryStats())
    # elif intent == 'Future Weather Forecast':
    #     return str(get_future_forecast(args,'2024-05-16'))
    return None

