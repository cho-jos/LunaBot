# following along https://realpython.com/how-to-make-a-discord-bot-python/ with some help from comment section
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents = discord.Intents(2048)
intents = discord.Intents.default()
intents.messages = True

# get client object from discord.py. Client is synonymouse with bot
client = discord.Client(intents=intents)

# listener for when the bot has switched from offline to online
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hello!':
        response = f'Hello, {message.author.name}'
        #response = "meow!"
        await message.channel.send(response)

client.run(TOKEN)