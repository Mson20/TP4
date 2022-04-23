import discord
from discord.ext import commands

class Bienvenue(discord.ext.commands.Cog, name='Bienvenue module'):
    def init(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="Bienvenue")
    async def addhoc_play(self, ctx):
        await ctx.send(f'Bienvenue {ctx.author.name}')