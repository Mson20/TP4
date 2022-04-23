import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

client = discord.Client()
client.run(os.getenv("TOKEN"))
bot = commands.Bot(command_prefix="$")
bot.run(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command(name="testerase")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete() 