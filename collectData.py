###########################################################################################
#
# Creation Date: 
###########################################################################################
# Weather Read Setup
import ipinfo
import requests
import json
import os
from dotenv import load_dotenv

url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric"

###########################################################################################
# Function: getKeys
# Note: .env File Containing both Variable Keys Must be Created First.
# Returns: Weather and IP API Keys Read from File.
def getKeys():
    load_dotenv()
    apiKeyIP = os.getenv('APIKEYIP')
    apiKeyWE = os.getenv('APIKEYWE')
    if apiKeyIP is None or apiKeyWE is None:
        raise ValueError("Expected Keys Not in .env File")
    else: return apiKeyIP, apiKeyWE

# Function: readCoords
# Returns: Location in Latitude and Longitude Coordinates.
def readCoords(key):
    handler = ipinfo.getHandler(key)
    details = handler.getDetails()
    return details.latitude, details.longitude

# Function: readWeather
# Returns: Selected Location Specific Weather Data.    
def readWeather(lat, lon, key, url):
    link = url % (lat, lon, key)
    response = requests.get(link)
    return json.loads(response.text)

# Function: weatherFunction
# Returns: 
def weatherFunction():
    apiKeyIP, apiKeyWE = getKeys()
    latitude, longitude = readCoords(apiKeyIP)
    weather = readWeather(latitude, longitude, apiKeyWE, url)
    print(weather)

###########################################################################################
weatherFunction()