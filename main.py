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


def get_data():
    """Will use parameters and endpoint to check Openweathermap API return list"""
    response = requests.get(OWM_ENDPOINT, params=PARAMETERS)
    response.raise_for_status()
    raw_data = response.json()
    return raw_data["list"][0:4]


def rain_check(list_data_elements):
    """will use list data from get_data and return true/false if rain is detected"""
    rain = False
    weather_list = ["rain" for item in list_data_elements if item["weather"][0]["id"] < 700]
    if "rain" in weather_list:
        rain = True
    return rain


if rain_check(get_data()):
    print("Bring an umbrella")
