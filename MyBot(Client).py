import discord
from discord import Client

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

client.run("OTU5MzQ5MjY0ODMwNTgyODA0.YkaloA.z-kcD2GSZMFAWuvy9w9XHD6Ggcg")