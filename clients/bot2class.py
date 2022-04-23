import discord
from discord.ext import commands

class Botstart(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} is on fire!!!!!')
    
    # classe qui va être utiliser dans botclass qui permet d'afficher le nom d'utilisateur suivi d'une phrase par le bot grâce à une commande 