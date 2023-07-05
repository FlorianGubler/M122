#!/usr/bin/python3
import logging
import modules.config
import modules.api.nba
import modules.api.football
import modules.pdf.reportPDF

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
season = "2023"
### FOOTBALL API
#APIDATA.append(modules.api.football.loaddata(CONFIG['api']['football']['properties']['league'], season, CONFIG['api']['football']['url'], CONFIG['cred']['apikeys']['football']))
### NBA API
#APIDATA.append(modules.api.nba.loaddata(season, CONFIG['api']['nba']['url'], CONFIG['cred']['apikeys']['nba']))

### Generate PDF Report
modules.pdf.reportPDF.generatePDFReport(CONFIG['pdf']['template'], CONFIG['pdf']['tmpfile']);
