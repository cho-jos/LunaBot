import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to Discord!')

@bot.event
async def on_message(message):
    if message.content.lower() == 'hello!':
        await message.channel.send(f'Hello, {message.author.name}')

# TODO: move slash commands to external files (cogs?)
@bot.slash_command(name='meow')
async def meow(ctx: discord.ApplicationContext):
    await ctx.respond('meow!')

bot.run(os.getenv('DISCORD_TOKEN'))