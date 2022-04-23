import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

client = discord.Client()
client.run(os.getenv("TOKEN"))

# Si on envoit par git cela sera visible sur github. Pour éviter cela on créer un fichier configuration sans extension qui permet de stocker le token.