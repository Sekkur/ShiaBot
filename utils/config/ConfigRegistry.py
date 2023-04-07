import json

from utils.Singleton import Singleton
from .Config import Config


class ConfigRegistry(Singleton):

    def __init__(self, configs: dict[str, Config] = None):
        self.configs = configs

    def get(self, config: str):
        return self.configs.get(config)

    def save(self):
        with open("../../resources/config.json") as file:
            print(json.dumps(self.configs))
            file.write(json.dumps(self.configs))
