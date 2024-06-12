from configparser import ConfigParser

def read_configuration(category, key):
    config = ConfigParser()
    config.read("Configuration/config.ini")
    config.get(category, key)
