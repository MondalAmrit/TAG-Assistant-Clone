import webbrowser, urllib.parse

def play_song(search_type, search_value):
    if search_type not in ('artist','song','album','playlist','podcast'):   search_type = 'song'
    url = "https://www.jiosaavn.com/search/" + urllib.parse.quote(search_type) + '/' + urllib.parse.quote(search_value)
    webbrowser.open(url)

functionMap = {
    1: play_song,
}