#!/usr/bin/python3
import requests
import yaml
import logging

# Variables
CONFIG_PATH = "./config/config.yaml"
LOG_LEVEL = logging.INFO

# Functions
def loadconfig():
    with open(CONFIG_PATH, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

# Configuration
## LoadConfig
CONFIG = loadconfig()

## SetupLogging
logger = logging.getLogger("MainLogger")
logger.setLevel(LOG_LEVEL)
fh = logging.FileHandler(CONFIG['logging']['file'])
fh.setLevel(LOG_LEVEL)
logger.addHandler(fh)

# Script
logger.info("Setup finished - Starting script")
## Get API Data
APIDATA = []
### FOOTBALL API
querystring = {"league":"39","season":"2023"}
headers = {
  "X-RapidAPI-Key": "067f9bd1aemsh0e4a61e4cfc7512p1aed22jsndbca7644"
}
response = requests.get(url, headers=headers, params=querystring)
APIDATA.append(response.json())
### NBA API
url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
querystring = {"id":"236","season":"2023"}
headers = {
	"X-RapidAPI-Key": "067f9bd1aemsh0e4a61e4cfc7512p1aed22jsndbca7644ec32",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
