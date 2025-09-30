from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData
load_dotenv()
import os
import requests
import time
FALLBACK_CODES = {
    "Dublin": "DUB",
    "Tokyo": "TYO",
    "Hong Kong": "HKG",
    "Kuala Lumpur": "KUL"
}

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = None
        self._get_new_token()   # get token immediately

    def _get_new_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        json_data = response.json()
        self._token = json_data["access_token"]
        print("✅ New Amadeus token acquired")



    def get_destination_code(self, city_name):
        if not self._token:
            self._get_new_token()

        url = "https://test.api.amadeus.com/v1/reference-data/locations"
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {"keyword": city_name, "subType": "CITY"}

        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 401:
                self._get_new_token()
                return self.get_destination_code(city_name)

            if response.status_code == 429:
                print("⚠️ Rate limit hit, waiting 5s...")
                time.sleep(5)
                return self.get_destination_code(city_name)

            response.raise_for_status()
            data = response.json().get("data", [])

            if data:
                return data[0]["iataCode"]
            else:
                if city_name in FALLBACK_CODES:
                    print(f"⚠️ Using fallback for {city_name}")
                    return FALLBACK_CODES[city_name]

                print(f"⚠️ No IATA code found for {city_name}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching IATA for {city_name}: {e}")
            return None

    def search_flights(self, origin_code, destination_code):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }

        tomorrow = datetime.now() + timedelta(days=1)
        return_date = tomorrow + timedelta(days=7)  # 1 week trip

        body = {
            "currencyCode": "GBP",
            "originDestinations": [
                {
                    "id": "1",
                    "originLocationCode": origin_code,
                    "destinationLocationCode": destination_code,
                    "departureDateTimeRange": {
                        "date": tomorrow.strftime("%Y-%m-%d")
                    }
                },
                {
                    "id": "2",
                    "originLocationCode": destination_code,
                    "destinationLocationCode": origin_code,
                    "departureDateTimeRange": {
                        "date": return_date.strftime("%Y-%m-%d")
                    }
                }
            ],
            "travelers": [
                {
                    "id": "1",
                    "travelerType": "ADULT"
                }
            ],
            "sources": ["GDS"],
            "searchCriteria": {
                "flightFilters": {
                    "connectionRestriction": {
                        "nonStopPreferred": True
                    }
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=body)  # ✅ fixed
            response.raise_for_status()
            data = response.json().get("data", [])

            if not data:
                return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

            offer = data[0]  # cheapest offer (Amadeus sorts by relevance/price)
            price = offer["price"]["total"]

            itinerary = offer["itineraries"][0]["segments"][0]
            origin_airport = itinerary["departure"]["iataCode"]
            destination_airport = itinerary["arrival"]["iataCode"]
            out_date = itinerary["departure"]["at"].split("T")[0]

            return_itinerary = offer["itineraries"][1]["segments"][0]
            return_date = return_itinerary["departure"]["at"].split("T")[0]

            return FlightData(price, origin_airport, destination_airport, out_date, return_date)

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching flights {origin_code} → {destination_code}: {e}")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
