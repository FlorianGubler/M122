#!/usr/bin/python3
import requests

# Variables
url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
querystring = {"id":"236","season":"2023"}

headers = {
	"X-RapidAPI-Key": "78b281d2b4msh199334df031c217p10b9b9jsne3f21c135a2c",

	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

#GET statistics
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
exit()
