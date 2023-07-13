#!/bin/bash

# Variables

LOG_LEVEL="INFO"


# Configuration

# LoadConfig

CONFIG=$(python3 -c "from modules import config; print(config.loadconfig())")

# SetupLogging

touch "${CONFIG['logging']['file']}"

python3 -c "import logging; logging.basicConfig(filename='${CONFIG['logging']['file']}', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.${LOG_LEVEL}, datefmt='%Y-%m-%d %H:%M:%S')"


# SCRIPT

try {

    logging.info("Setup finished - Starting script")

    # Get API Data

    APIDATA=()

    # FOOTBALL API

    # APIDATA['football']=$(python3 -c "from modules.api import football; import datetime; print(football.loaddata(${CONFIG['api']['football']}, datetime.date.today().year, ${CONFIG['cred']['apikeys']['football']}))")

    # NBA API

    APIDATA['nba']=$(python3 -c "from modules.api import nba; print(nba.loaddata(${CONFIG['api']['nba']}, ${CONFIG['cred']['apikeys']['nba']}))")

    # Generate PDF Report

    #python3 -c "from modules.pdf import reportPDF; reportPDF.generatePDFReport(${CONFIG['pdf']}, ${APIDATA})"

    # Send Mail Report

    #python3 -c "from modules.mail import manageMail; manageMail.send_email(${CONFIG['smtp']}, ${CONFIG['pdf']['tmpfile']}, ${CONFIG['cred']['mail']['password']})"

    # Send Report via FTP to Server

    #python3 -c "from modules.ftp import sendFTP; sendFTP.send_ftp(${CONFIG['ftp']}, ${CONFIG['pdf']['tmpfile']}, ${CONFIG['cred']['ftp']['password']})"

} catch {

    logging.error("An Exception occured: $([[ $- = *e* ]] && echo $BASH_COMMAND)")

    python3 -c "from modules.mail import manageMail; manageMail.send_error_email(${CONFIG['smtp']}, $([[ $- = *e* ]] && echo $BASH_COMMAND), ${CONFIG['cred']['mail']['password']})"

}
