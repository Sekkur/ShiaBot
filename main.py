import json
import logging
import discord
from utils.InstanceStorage import InstanceStorage
from utils.config.JSONConfig import JSONConfig
from features.admin.AdminConfig import AdminConfig
from typing import Any

intents = discord.Intents.all()
client = discord.Client(intents=intents)
discord.utils.setup_logging(level=logging.INFO, root=False)

FILE_PATH = "resources/config.json"
storage = InstanceStorage()
storage.add(JSONConfig(FILE_PATH))
config = storage.get(JSONConfig.__name__)
print(config)
print(InstanceStorage._self.get(JSONConfig.__name__))

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


client.run("MTA5MzkyNzA4Njk5MDgyNzY1Mg.GlHqHZ.OR_qCJBoeNIttqRsx8GfXkaQeyPRgPkrkvfrCY")
