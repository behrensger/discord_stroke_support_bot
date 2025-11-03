import os

import discord
import logging
import datetime
from dotenv import load_dotenv
logger = logging.getLogger(__name__)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        username = str(message.author).split("#")[0]
        channel = str(message.channel.name)
        user_message = message.content.lower()
        logger.info(f'Incoming Message {user_message} by {username} on {channel}')

        if message.author == client.user:
            return

        if user_message.count("proto"):
            split = user_message.split()
            today = datetime.datetime.now()
            if not os.path.isfile(f'{username}.csv'):
                with open(f'{username}.csv', "a", encoding="utf-8") as f:
                    f.write("username,today,systolic,diastolic\n")
            with open(f'{username}.csv', "a", encoding="utf-8") as f:
                f.write(f'{username},{today.isoformat()},{split[1].strip()}, {split[2].strip()}\n')
            await message.channel.send(f'Wrote Protokol: {split[1]}, {split[2]} and timestap: {today}')
            logger.info(f'Protokoll: {username} for {split[1]}, {split[2]} and {today}')


#############################################
# inital load
load_dotenv()
intents = discord.Intents.default() # create a default Intents instance
intents.message_content = True # enable message content intents
client = MyClient(intents= intents)
logging.basicConfig(level=logging.INFO)

token = os.getenv('DISCORD_TOKEN')
if token is None:
    print('Token DISCORD_TOKEN not found!')
    exit(-1)
client.run(token)
