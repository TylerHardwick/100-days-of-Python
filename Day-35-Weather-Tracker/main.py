import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os



LATITUDE = 52.234840
LONGITUDE = -0.897320
MY_PHONE_NUM = "123"
SEND_PHONE_NUM = "456"
OWM_API_KEY = "OMW Api here"
ACCOUNT_SID_KEY = "SID HERE"
AUTH_TOKEN_KEY = "Authentification token here"

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID_KEY")
auth_token = os.environ.get("AUTH_TOKEN_KEY")



parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
daily_forecast_list = [weather_data["list"][num]["weather"][0]["id"] for num in range(0, 5)]


rain_today = False
for item in daily_forecast_list:
    if item < 700:
        rain_today = True
if rain_today:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Hey Tyler, it's going to rain today. Remember to bring an umbrella ☔.",
        from_= SEND_PHONE_NUM,
        to= MY_PHONE_NUM
    )
    print(message.status)