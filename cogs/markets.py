import discord
from discord.ext import commands

class MarketsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.command()
    async def hello(self, ctx):
        await ctx.respond('hello, I am the markets cog.')

def setup(bot):
    bot.add_cog(MarketsCog(bot))