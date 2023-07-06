import yaml
import logging

CONFIG_PATH = "./config/config.yaml"
CRED_CONFIG_PATH = "../../cred.yml"

def loadconfig():
    with open(CONFIG_PATH, "r") as stream:
        config = yaml.safe_load(stream)
        with open(CRED_CONFIG_PATH, "r") as cred_stream:
            config["cred"] = yaml.safe_load(cred_stream)
            return config
