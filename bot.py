import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = discord.Bot(intents=intents)

cogs = ['cogs.reminders', 'cogs.markets']
for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to Discord!')

@bot.event
async def on_message(message):
    if message.content.lower() == 'hello!':
        await message.channel.send(f'Hello, {message.author.name}')

bot.run(TOKEN)