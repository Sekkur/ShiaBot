import logging
import discord
from utils import common

intents = discord.Intents.all()
client = discord.Client(intents=intents)
discord.utils.setup_logging(level=logging.INFO, root=False)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

client.run(common.token)
