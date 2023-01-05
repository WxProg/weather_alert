import requests
import os
from dotenv import load_dotenv

# Create and access an environment variable file (.env)
load_dotenv(".env")

# Store my open weather map api in the .env file
api_key = os.getenv("API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
weather_parameters = {
    "lat": 30.468580,
    "lon": -83.410049,
    "appid": api_key,
    "units": "imperial",
    "exclude": "minutely,daily,current"
}

response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
hourly_forecast = weather_data["hourly"]
forecast_12hour = hourly_forecast[:12]
weather_conditions_12hour_codes = [hour["weather"][0]["id"] for hour in forecast_12hour]

will_rain = False
for code in weather_conditions_12hour_codes:
    if code < 700:
        will_rain = True
if will_rain:
    print("Rain")
