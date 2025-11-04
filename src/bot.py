import os

import discord
import logging
import datetime
import re
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
            today = datetime.datetime.now()
            split = re.split(r'[+,.\s]+', user_message.strip())
            if len(split) != 3 and split[0] != 'proto':
                await message.channel.send(
                    f'Cannot write protocol because values will not be understood')
                return
            sys = int(split[1].strip())
            dis = int(split[2].strip())
            if sys < 80 or dis > 270 or dis < 60 or dis > 100:
                await message.channel.send(f'Cannot write protocol because values {sys} or {dis} either to big or to small')
                return
            if not os.path.isfile(f'{username}.csv'):
                with open(f'{username}.csv', "a", encoding="utf-8") as f:
                    f.write("username,today,systolic,diastolic\n")
            with open(f'{username}.csv', "a", encoding="utf-8") as f:
                f.write(f'{username},{today.isoformat()},{sys}, {dis}\n')
            await message.channel.send(f'Wrote Protokol: {sys}, {dis} on {today.strftime("%d. %B %Y %I:%M%p")}')


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
