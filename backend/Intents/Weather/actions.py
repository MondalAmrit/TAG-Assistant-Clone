"""
API guides taken from,

https://www.weatherapi.com/my/

"""

import os, requests, pprint

base_url = f"http://api.weatherapi.com/v1/"
add_url = f".json?key={os.getenv('weather_api')}"

def get_current(Location):
    return requests.get(base_url + 'current' + add_url + f'&q={Location}&aqi=yes').json()
    
def get_forecast(Location, days = 3):
    return requests.get(base_url+ 'forecast' + add_url + f'&q={Location}&days=3&aqi=yes&alerts=yes').json()

def get_coords(Location):
    return requests.get(base_url + 'search' + add_url + f'&q={Location}')

def get_history(Location, date, time = None):
    """
    Returns the previous forecasts. (Limited till previous year)
    attributes
    ----------
    Location: str 
    date: str (In YYYY-MM-DD)
    time: str (In 24 hour) (Use 0 if single digit) (Ex: 01:53)

    Outputs
    --------
    Json data
    """
    response = requests.get(base_url + 'future' + add_url + f'&q={Location}&dt={date}').json()

    if time is not None:
        return response['forecast']['forecastday']['hour'][date + ' ' + time]
    else:
        return response['forecast']['forecastday'][0]['day']
    
def get_future_forecast(Location, date, time = None):
    """
    Returns the future forecasts. (Limited till future year)
    attributes
    ----------
    Location: str 
    date: str (In YYYY-MM-DD)
    time: str (In 24 hour) (Use 0 if single digit) (Ex: 01:53)

    Outputs
    --------
    Json data
    """
    response = requests.get(base_url + 'history' + add_url + f'&q={Location}&dt={date}').json()

    if time is not None:
        return response['forecast']['forecastday']['hour'][date + ' ' + time]
    else:
        return response['forecast']['forecastday'][0]['day']
    
def get_astronomy(Location, date):
    return requests.get(base_url + 'astronomy' + add_url + f'&q={Location}&dt={date}').json()

functionMap = {
    1: get_current,
    2: get_coords,
    3: get_history,
    4: get_future_forecast,
    5: get_astronomy,
}

# pprint.pprint(get_current('new delhi'))