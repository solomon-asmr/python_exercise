import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Read from .env
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

HEADERS = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Get data from Google Sheet"""
        response = requests.get(SHEETY_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Update each row in Google Sheet with its IATA code"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"
            response = requests.put(url=put_endpoint, json=new_data, headers=HEADERS)
            response.raise_for_status()
            print(f"Updated row {city['id']} → {city['city']} with IATA: {city['iataCode']}")
