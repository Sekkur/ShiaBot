import json
from abc import ABC

from .Config import Config
from typing import Any


class JSONConfig(Config):
    def __init__(self, path: str):
        data: dict[Any, Any] = dict[Any, Any]()
        super().__init__(path, data)
        with open(path) as file:
            json_data = json.load(file)
            if isinstance(json_data, dict):
                self.data = json_data

    def save(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file)
