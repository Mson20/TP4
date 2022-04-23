import discord
from discord.ext import commands

class Botstart(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} is on fire!!!!!')