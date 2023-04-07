import json
import logging
import discord
from utils.InstanceStorage import InstanceStorage

intents = discord.Intents.all()
client = discord.Client(intents=intents)
discord.utils.setup_logging(level=logging.INFO, root=False)

storage = InstanceStorage()
jsonData = json.load()
@client.event()
async def on_ready():
    print(f"We have logged in as {client.user}")


client.run("MTA5MzkyNzA4Njk5MDgyNzY1Mg.GlHqHZ.OR_qCJBoeNIttqRsx8GfXkaQeyPRgPkrkvfrCY")
