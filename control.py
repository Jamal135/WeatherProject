# Control operations of weather data program.
from collect_data import weather_function
from json import load

# Function: load_config
def load_config():
    with open("configuration.json") as data:
        return load(data)

configuration = load_config()
data = weather_function(configuration)