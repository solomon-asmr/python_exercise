import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()
data = response.json()["iss_position"]
latitude=data["latitude"]
longitude=data["longitude"]
iss_position = (latitude, longitude)
print(iss_position)