import yaml

CONFIG_PATH = "./config/config.yaml"

def loadconfig():
    with open(CONFIG_PATH, "r") as stream:
        return yaml.safe_load(stream)
