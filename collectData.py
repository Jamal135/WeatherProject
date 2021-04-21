# Pull selected location specific weather information using open weather and ipinfo.
from os import getenv
from json import loads
from requests import get
from ipinfo import getHandler
from dotenv import load_dotenv

# Open weather link to manipulate for weather data.
URL = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric"

# Function: get_keys
# Note: .env file containing both keys must be present.
def get_keys():
    """ Returns: Weather and IP API keys read from stored .env file. """
    load_dotenv()
    api_key_ip = getenv('APIKEYIP')
    api_key_weather = getenv('APIKEYWE')
    if api_key_ip is None or api_key_weather is None:
        raise ValueError("Expected Keys Not in .env File")
    else: return api_key_ip, api_key_weather

# Function: read_coords
def read_coords(key):
    """ Returns: Location coordinates in latitude and longitude from ipinfo. """
    handler = getHandler(key)
    details = handler.getDetails()
    return details.latitude, details.longitude

# Function: read_weather
def read_weather(lat, lon, key):
    """ Returns: Selected location specific weather data from open weather. """
    link = URL % (lat, lon, key)
    response = get(link)
    return loads(response.text)

# Function: pull_data
# Note: Selected data to be pulled is defined in the .env file.
def pull_data(weather):
    """ Returns: Selected information from complete weather data. """
    pass

# Function: weather_function
def weather_function():
    """ Returns: Selected location specific weather information & data. """
    api_key_ip, api_key_weather = get_keys()
    latitude, longitude = read_coords(api_key_ip)
    weather_data = read_weather(latitude, longitude, api_key_weather)
    return pull_data(weather_data)

weather_function()