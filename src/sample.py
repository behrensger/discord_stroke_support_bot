import discord
import json
import random

intents = discord.Intents.default()
client = discord.Client(intents=intents)

sad_words = ["sad", "miserable"]
starter_encouragements = [
  "Hang in there!",
  "You‘ve got this!"
]

def get_quote():
  # Code from before

@client.event
async def on_ready():
    print(f'{client.user} is ready!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragements
    if "encouragements" in data:
        options.extend(data["encouragements"])

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ")[1]
        startup_extensions.append(encouraging_message)

        await message.channel.send("New encouraging message added.")

client.run("TOKEN")