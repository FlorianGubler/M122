import requests

def loaddata(league, season, url, apikey):
  querystring = {"league":league,"season":season}
  headers = {
    "X-RapidAPI-Key": apikey
  }
  return requests.get(url, headers=headers, params=querystring).json()
