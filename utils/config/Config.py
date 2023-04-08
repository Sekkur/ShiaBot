import abc
from typing import Any


class Config(metaclass=abc.ABCMeta):

    def __init__(self, path: str, data: dict[Any, Any]):
        self.path = path
        self.data: dict[Any, Any] = data

    def addCategory(self, key: Any, value: Any) -> None:
        self.data.update({key: value})

    def hasCategory(self, key: Any) -> bool:
        return isinstance(self.get(key), dict)

    def get(self, key: Any) -> Any:
        return self.data.get(key)

    def getAll(self) -> dict[Any, Any]:
        return self.data

    @abc.abstractmethod
    def save(self):
        return
