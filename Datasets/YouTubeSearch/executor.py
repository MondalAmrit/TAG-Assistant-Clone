import webbrowser, urllib.parse

def YT_search(query):
    # https://www.youtube.com/results?search_query=pewdiepie
    url = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(query)
    webbrowser.open(url)

functionMap = {
    1: YT_search,
}