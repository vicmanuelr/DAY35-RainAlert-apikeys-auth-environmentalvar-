import requests
from twilio.rest import Client
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "20e48b5ebf465fc69d4befd150b459db"
PARAMETERS = {
    'lat': 14.6407,
    'lon': -90.5133,
    "units": "metric",
    "cnt": 4,
    "appid": API_KEY,
}

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)



def get_data():
    """Will use parameters and endpoint to check Openweathermap API return list"""
    response = requests.get(OWM_ENDPOINT, params=PARAMETERS)
    response.raise_for_status()
    raw_data = response.json()
    return raw_data["list"][:4]  # this equals 4 elements of 3 hours forecast each, total 12 hours


def rain_check(list_data_elements):
    """will use list data from get_data and return true/false if rain is detected"""
    rain = False
    weather_list = ["rain" for item in list_data_elements if item["weather"][0]["id"] < 700]
    if "rain" in weather_list:
        rain = True
    return rain


if rain_check(get_data()):
    print("Bring an umbrella")
