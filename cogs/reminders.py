import discord
from discord.ext import commands

class RemindersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.command()
    async def meow(self, ctx):
        await ctx.respond('meow!')

def setup(bot):
    bot.add_cog(RemindersCog(bot))