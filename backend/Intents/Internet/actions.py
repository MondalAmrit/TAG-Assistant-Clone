import webbrowser, urllib.parse

def get_info(query):
    query_page = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(query_page)

def open_url(url):
    web_url = "www." + url + ".com"
    webbrowser.open(web_url)

def get_image(query):
    img_page = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(img_page)

def get_product(query):
    product_page = "https://www.amazon.in/s?k=" + urllib.parse.quote(query)
    webbrowser.open(product_page)

functionMap = {
    1: get_info,
    2: open_url,
    3: get_image,
    4: get_product,
}