import requests
from datetime import datetime


# Choose a username and token
USERNAME = "YOURUSERNAME"         # must be unique
TOKEN = "YOURTOKEN"       # secret token to authenticate API requests

# Pixela user creation endpoint
pixela_endpoint = "YOURPIXELAENDPOINT"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


graph_id = "YOURGRAPHID"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : graph_id,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

#to check if its working on browser check this link
# https://pixe.la/v1/users/solomonkassahun1234/graphs/graph1.html


pixel_endpoint = f"{graph_endpoint}/{graph_id}"

yesterday = datetime(year=2025, month=9,day=29)
today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date" : yesterday.strftime("%Y%m%d"),
    "quantity" : input("how many kilometers did you cycle today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)



yesterday_stringify = yesterday.strftime("%Y%m%d")
update_pixel_endpoint = f"{pixel_endpoint}/{yesterday_stringify}"

update_config = {

    "quantity" : "4"
}
response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
print(response.text)



delete_pixel_endpoint = f"{pixel_endpoint}/{yesterday_stringify}"
response = requests.delete(url = delete_pixel_endpoint, headers=headers)
print(response.text)







