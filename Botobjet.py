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
#permet de supprimer grâce à une commande

#class TestBotClient(discord.Client):
#    async def on_ready(self):
#       print(f'{self.user} The bot is on fireeee!!!!!!!!')
#
#    async def on_message(self, message):
#        if self.user == message.author:
#            return
#
#        if message.content == "salut":
#            await message.channel.send('salut')

#client = CustomClient()
#client.run(os.getenv("TOKEN"))        


