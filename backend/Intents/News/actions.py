import requests 
from bs4 import BeautifulSoup 

def get_latest_news():
    url = 'https://timesofindia.indiatimes.com/home/headlines'
    response = requests.get(url) 

    print('Fetching the news from Times of India')
    soup = BeautifulSoup(response.text, 'html.parser') 
    r = soup.find('body').find_all('span',{"class":'w_tle'})
    headlines = []
    for i in r:
        s = i.find('a')
        headlines.append({"Headline":s.text.strip(),"Link": 'https://timesofindia.indiatimes.com/' + s['href']})
    return headlines[:10]
