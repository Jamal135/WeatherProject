""" Pull selected location specific weather information using open weather and ipinfo"""

from os import getenv
from json import loads
from requests import get
from ipinfo import getHandler
from dotenv import load_dotenv

url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric"

def get_keys():
    """
    Function: get_keys
    Note: .env file containing both variable keys must be created first.
    Returns: Weather and IP API keys read from .env file.
    """
    load_dotenv()
    api_key_ip = getenv('APIKEYIP')
    api_key_weather = getenv('APIKEYWE')
    if api_key_ip is None or api_key_weather is None:
        raise ValueError("Expected Keys Not in .env File")
    else: return api_key_ip, api_key_weather

def read_coords(key):
    """
    Function: read_coords
    Returns: Location coordinates in latitude and longitude.
    """
    handler = getHandler(key)
    details = handler.getDetails()
    return details.latitude, details.longitude

def read_weather(lat, lon, key, url):
    """
    Function: read_weather
    Returns: Selected location specific weather data.
    """
    link = url % (lat, lon, key)
    response = get(link)
    return loads(response.text)
 
def weather_function():
    """
    Function: weather_function
    Returns: 
    """
    api_key_ip, api_key_weather = get_keys()
    latitude, longitude = read_coords(api_key_ip)
    weather = read_weather(latitude, longitude, api_key_weather, url)
    print(weather)

weather_function()