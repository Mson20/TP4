import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

client = discord.Client()
client.run(os.getenv("TOKEN"))