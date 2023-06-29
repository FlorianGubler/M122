import requests

def loaddata(season, url, apikey):
  querystring = {"season":season}
  headers = {
    "X-RapidAPI-Key": apikey,
  }
  return requests.get(url, headers=headers, params=querystring).json()
