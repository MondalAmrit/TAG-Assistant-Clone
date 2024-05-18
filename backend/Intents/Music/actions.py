import webbrowser, urllib.parse

def play_song(search_value):
    if search_value == None or search_value == '':
        url = 'https://wynk.in/music'
    else:
        url = "https://www.jiosaavn.com/search/song/" + urllib.parse.quote(search_value)
    webbrowser.open(url)

functionMap = {
    1: play_song,
}