#!/usr/bin/python3
import modules.config
import modules.api.nba
import modules.api.football
import modules.pdf.reportPDF
import modules.mail.sendMail
import modules.ftp.sendFTP
import datetime
import logging

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
APIDATA = {}
### FOOTBALL API
APIDATA['football'] = modules.api.football.loaddata(CONFIG['api']['football'], datetime.date.today().year, CONFIG['cred']['apikeys']['football'])
### NBA API
APIDATA['nba'] = modules.api.nba.loaddata(CONFIG['api']['nba'], CONFIG['cred']['apikeys']['nba'])
### Generate PDF Report
modules.pdf.reportPDF.generatePDFReport(CONFIG['pdf'], APIDATA);
### Send Mail Report
modules.mail.sendMail.send_email(CONFIG['smtp'], CONFIG['pdf']['tmpfile'], CONFIG['cred']['mail']['password'])
### Send Report via FTP to Server
modules.ftp.sendFTP.send_ftp(CONFIG['ftp'], CONFIG['pdf']['tmpfile'], CONFIG['cred']['ftp']['password'])
