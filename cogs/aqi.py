import discord
from discord.ext import commands

class AqiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.command()
    async def aqi(self, ctx):
        await ctx.respond('aqi')
    
def setup(bot):
    bot.add_cog(AqiCog(bot))