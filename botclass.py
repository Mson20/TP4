import discord
from clients.bot2class import Botstart
from cogs.Bienvenue import Bienvenue
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

def main():
    

    intents = discord.Intents.default()
    intents.members = True

    bot = Botstart(
        command_prefix='$', 
        intents=intents
    )

    bot.add_cog(Bienvenue(bot))

    bot.run(os.getenv("TOKEN"))


if name == 'main':
    main() 