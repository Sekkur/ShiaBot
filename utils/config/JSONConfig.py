import json
from abc import ABC

from .Config import Config
from typing import Any


class JSONConfig(Config):
    def __init__(self, path: str):
        data: dict[Any, Any] = dict[Any, Any]()
        with open(path) as file:
            json_data = json.load(file)
            if isinstance(json_data, dict):
                data = json_data
        super().__init__(path, data)

    def getAll(self) -> dict[Any, Any]:
        return super().data

    def save(self):
        with open(super().path, "w") as file:
            json.dump(self.data, file)
