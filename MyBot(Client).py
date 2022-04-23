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
    # Affiche sur la console que le bot est prêt est donc un moyen pour savoir qu'on peut l'utiliser
  
@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(959348198969843735)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")
    # Affiche le message avec le nom d'utilisateur

@client.event
async def on_message(message):
    print(message.content)
    # Affiche le contenu du message


@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")
    # Commande qui permet de renvoyer Pong si Ping fonctionne

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    # Commande qui permet de supprimer selon le nombre ou chiffre choisi qui suit !del
    

client.run(os.getenv("TOKEN"))