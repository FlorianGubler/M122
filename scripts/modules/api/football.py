import requests
import logging

def loaddata(league, season, url, host, apikey):
  querystring = {"league":league,"season":season}
  headers = {
    "X-RapidAPI-Key": apikey,
    "X-RapidAPI-Host": host
  }
  response = requests.get(url, headers=headers, params=querystring)
  if response.status_code == 200:
    logging.info("Called Football API succesfully")
    return response.json()
  else:
    logging.error("Football API Call failed - Response: '" + response.text + "'") 
    raise Exception("Football API Call failed (StatusCode: " + str(response.status_code) + ")")
