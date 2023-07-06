import requests
import logging

def loaddata(config, apikey):
  logging.info("Loading NBA Data")
  querystring = {"tournamentId":config['properties']['tournamentId']}
  headers = {
    "X-RapidAPI-Key": apikey
  }
  response = requests.get(config['url'], headers=headers, params=querystring)
  if response.status_code == 200:
    logging.info("Called NBA API succesfully")
    return response.json()
  else:
    raise Exception("NBA API Call failed (StatusCode: " + str(response.status_code) + "), with Response: '" + response.text + "'")
