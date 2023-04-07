from abc import abstractmethod
from discord.ext.commands import Cog


class Feature:
    def __init__(self, name: str, description: str, cogs: list[Cog]):
        self.name = name
        self.description = description
        self.cogs = cogs
