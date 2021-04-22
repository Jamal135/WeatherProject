# Pull selected location specific weather information using open weather and ipinfo.
from os import getenv
from json import loads
from requests import get
from ipinfo import getHandler
from dotenv import load_dotenv

# Open weather links to manipulate for weather data.
URLCURRENT = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric"
URLFORECAST = "https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s&units=metric"

# Function: get_keys
# Note: .env file containing both keys must be present.
def get_keys():
    """ Returns: Weather and IP API keys read from stored .env file. """
    load_dotenv()
    key_ip = getenv('APIKEYIP')
    key_weather = getenv('APIKEYWE')
    if key_ip is None or key_weather is None:
        raise ValueError("Expected Keys Not in .env File")
    else: return key_ip, key_weather

# Function: read_coords
def read_coords(key):
    """ Returns: Location coordinates in latitude and longitude from ipinfo. """
    handler = getHandler(key)
    details = handler.getDetails()
    return details.latitude, details.longitude

# Function: weather_call
def weather_call(url):
    """ Returns: Data pulled from get request to specified URL. """
    response = get(url)
    return loads(response.content)

# Function: read_weather
def read_weather(lat, lon, key, number_days):
    """ Returns: Complete location specific weather data from open weather. """
    link_current = URLCURRENT % (lat, lon, key)
    data_current = weather_call(link_current)
    if number_days > 1:
        link_forecast = URLFORECAST % (lat, lon, key)
        data_forecast = weather_call(link_forecast)
        return data_current, data_forecast
    else: return data_current, None

# Function: pull_data
# Note: Selected data to be pulled is defined in the configuration JSON file.
def pull_data(current, forecast, configuration):
    """ Returns: Selected information from complete weather data. """
    pass

# Function: weather_function
def weather_function(configuration):
    """ Returns: Selected location specific weather information & data. """
    number_days = int(configuration["days"])
    key_ip, key_weather = get_keys()
    latitude, longitude = read_coords(key_ip)
    current, forecast = read_weather(latitude, longitude, key_weather, number_days)
    return pull_data(current, forecast, configuration)