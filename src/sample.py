import os

import discord
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {messsage.author}: {message.content}')

load_dotenv()
client = MyClient(intents=discord.Intents.default())
token = os.getenv('DISCORD_TOKEN')
if token is None:
    print('Token DISCORD_TOKEN not found!')
    exit(-1)
client.run(token)
