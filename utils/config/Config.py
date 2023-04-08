import abc
from typing import Any


class Config(metaclass=abc.ABCMeta):

    def __init__(self, path: str, data: dict[Any, Any]):
        self.path = path
        self.data: dict[Any, Any]() = data

    def set(self, key: Any, value: Any) -> None:
        self.data.update({key: value})

    def get(self, key: Any) -> Any:
        return self.data.get(key)

    @abc.abstractmethod
    def getAll(self):
        return

    @abc.abstractmethod
    def save(self):
        return
