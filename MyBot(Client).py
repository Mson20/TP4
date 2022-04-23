import discord
from discord import Client
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot esy prêt.")
  
@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(959348198969843735)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

@client.event
async def on_message(message):
    print(message.content)

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

client.run(os.getenv("TOKEN"))