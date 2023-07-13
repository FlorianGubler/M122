#!/usr/bin/python3
import logging
import modules.config
import modules.api.nba

# Variables
LOG_LEVEL = logging.INFO

# Configuration
## LoadConfig
CONFIG = modules.config.loadconfig()

## SetupLogging
with open(CONFIG['logging']['file'], 'w'):
    pass
logging.basicConfig(
    filename=CONFIG['logging']['file'],
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=LOG_LEVEL,
    datefmt='%Y-%m-%d %H:%M:%S')

# Script
logging.info("Setup finished - Starting script")
## Get API Data
APIDATA = []
### BASKETBALL API
APIDATA.append(modules.api.nba.loaddata(CONFIG['api']['nba']['properties']['tournamentId'], CONFIG['api']['nba']['url'], CONFIG['cred']['apikeys']['nba']))
print(APIDATA)
