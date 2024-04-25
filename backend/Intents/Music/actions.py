import webbrowser, urllib.parse

def play_song(search_value):
    url = "https://www.jiosaavn.com/search/song/" + urllib.parse.quote(search_value)
    webbrowser.open(url)

functionMap = {
    1: play_song,
}