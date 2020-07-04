import configparser

class SLOBSConfig():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')