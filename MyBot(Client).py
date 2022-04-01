import discord
from discord import Client

client = discord.Client()
client.run("OTU5MzQ5MjY0ODMwNTgyODA0.YkaloA.qvbtt98FlWGbHpmdXZ9hdqOufiA")


class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")