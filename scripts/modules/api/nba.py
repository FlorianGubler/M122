import requests
import logging

def loaddata(config, season, apikey):
  querystring = {"season":season}
  headers = {
    "X-RapidAPI-Key": apikey,
    "X-RapidAPI-Host": config['host']
  }
  response = requests.get(config['url'], headers=headers, params=querystring)
  if response.status_code == 200:
    logging.info("Called NBA API succesfully")
    return response.json()
  else:
    logging.error("NBA API Call failed - Response: '" + response.text + "'")
    raise Exception("NBA API Call failed (StatusCode: " + str(response.status_code) + ")")
