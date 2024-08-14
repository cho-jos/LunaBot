import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True

# get client object from discord.py. Client is synonymous with bot
bot = discord.Client(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(bot) # tree holds all the application commands

# listener for when the bot has switched from offline to online
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'hello!':
        response = f'Hello, {message.author.name}'
        await message.channel.send(response)

# TODO: extract slash commands to another file?
# slash commands
bot.load_extension()
# @tree.command(name='meow')
# async def meow(interaction: discord.Interaction):
#     await interaction.response.send_message("meow!")

bot.run(TOKEN)