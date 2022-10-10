import requests
import datetime as dt

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "20e48b5ebf465fc69d4befd150b459db"
PARAMETERS = {
    'lat': 14.6407,
    'lon': -90.5133,
    "units": "metric",
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
data = response.json()
print(data)
