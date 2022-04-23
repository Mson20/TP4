import discord
from discord.ext import commands


client = discord.Client()
client.run("VOTRE TOKEN ICI")
bot = commands.Bot(command_prefix="!")
bot.run("VOTRE TOKEN ICI")

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete() 