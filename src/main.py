#!/usr/bin/python3
import modules.config
import modules.api.nba
import modules.api.football
import modules.pdf.reportPDF
import modules.mail.manageMail
import modules.ftp.sendFTP
import datetime
import logging
import os

# Variables
LOG_LEVEL = logging.INFO

# Configuration
## LoadConfig
CONFIG = modules.config.loadconfig()

## Create required folders exist
requiredDirs = CONFIG['required']['dirs']
for dir in requiredDirs:
  if not os.path.exists(dir):
    os.makedirs(dir)

## SetupLogging
logging.basicConfig(
    filename=CONFIG['logging']['file'],
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=LOG_LEVEL,
    datefmt='%Y-%m-%d %H:%M:%S')

## SCRIPT
try:
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
    modules.mail.manageMail.send_email(CONFIG['smtp'], CONFIG['pdf']['tmpfile'], CONFIG['cred']['mail']['password'])
    ### Send Report via FTP to Server
    modules.ftp.sendFTP.send_ftp(CONFIG['ftp'], CONFIG['pdf']['tmpfile'], CONFIG['cred']['ftp']['password'])
except Exception as e:
    logging.error("An Exception occured: " + ''.join(traceback.TracebackException.from_exception(e).format()))
    modules.mail.manageMail.send_error_email(CONFIG['smtp'], e, CONFIG['cred']['mail']['password'])
