# Control operations of weather data program.
from collect_data import weather_function
from json import load

# Function: load_config
def load_config():
    """ Returns: JSON configuration file as a loaded dictionary. """
    with open("configuration.json") as data:
        return load(data)

configuration = load_config()
data = weather_function(configuration)
print(data)