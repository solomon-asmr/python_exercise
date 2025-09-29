import requests
import os
from twilio.rest import Client

# ----------------------------
# Load secrets from environment
# ----------------------------
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
OWM_API_KEY = os.getenv("OWM_API_KEY")

if not all([AUTH_TOKEN, ACCOUNT_SID, OWM_API_KEY]):
    raise ValueError("One or more environment variables are missing!")

# ----------------------------
# OpenWeatherMap API
# ----------------------------
api_key = OWM_API_KEY
parameters = {
    "lat": 31.243870,
    "lon": 34.793991,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

# ----------------------------
# Twilio client
# ----------------------------
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ----------------------------
# Check weather forecast
# ----------------------------
will_rain = False
for i in range(4):
    forecast_id = response.json()["list"][i]["weather"][0]["id"]
    print(f"Forecast ID {i}: {forecast_id}")
    if forecast_id < 700:
        will_rain = True

# ----------------------------
# Send WhatsApp message
# ----------------------------
if will_rain:
    print("Bring an umbrella ☔")
    message = client.messages.create(
        from_="whatsapp:+123456789",  # your Twilio WhatsApp number
        body="It's going to rain today, you need to bring an umbrella ☔",
        to="whatsapp:+098765432",  # your phone number
    )
else:
    print("No rain today 🌞")
    message = client.messages.create(
        from_="whatsapp:+14155238886",  # your Twilio WhatsApp number
        body="It's not going to rain today, you don't need to bring an umbrella",
        to="whatsapp:+972537828854",  # your phone number
    )

print(f"Message status: {message.status}")

# ----------------------------
# Instructions
# ----------------------------
"""
To set environment variables in Git Bash:
    export TWILIO_AUTH_TOKEN=your_auth_token
    export TWILIO_ACCOUNT_SID=your_account_sid
    export OWM_API_KEY=your_openweathermap_api_key

To check environment variables:
    env
"""
