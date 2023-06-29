import requestsimport yaml
import logging

# Variables
CONFIG_PATH = "./config/config.yaml"
LOG_LEVEL = logging.INFO

# Functions
def loadconfig():
	 with open(CONFIG_PATH,"r") as stream:
		try:
			 return yaml.safe_load(stream)
 		except yaml.YAMLError as exc:
		            print(exc)
# Configuration
##LoadConfig
CONFIG = loadconfig()
## SetupLogging
logger = logging.getLogger("MainLogger")logger.setLevel(LOG_LEVEL)
# Create Logging file
handlerfh = logging.FileHandler(CONFIG['logging']['file'])fh.setLevel(LOG_LEVEL) logger.addHandler(fh)
# Script
logger.info("Setup finished - Starting script")
