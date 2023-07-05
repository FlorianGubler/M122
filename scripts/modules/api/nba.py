import requests
import logging

def loaddata(season, url, apikey):
  querystring = {"season":season}
  headers = {
    "X-RapidAPI-Key": apikey,
  }
  response = requests.get(url, headers=headers, params=querystring)
  if response.status_code == 200:
    logging.info("Called NBA API succesfully")
    return response.json()
  else:
    logging.error("NBA API Call failed - Response: " + str(response))
    raise Exception("NBA API Call failed (StatusCode: " + str(response.status_code) + ")")
