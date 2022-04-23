import discord
from clients.bot2class import Botstart
from cogs.greetings import Greetings

def main():
    token = "OTU5MzQ5MjY0ODMwNTgyODA0.YkaloA.V66VtfB-z1q3qrPtGyBSjx5hBsI"


    intents = discord.Intents.default()
    intents.members = True

    bot = Botstart(
        command_prefix='$', 
        intents=intents
    )

    bot.add_cog(Greetings(bot))

    bot.run(OTU5MzQ5MjY0ODMwNTgyODA0.YkaloA.V66VtfB-z1q3qrPtGyBSjx5hBsI)


if name == 'main':
    main() 