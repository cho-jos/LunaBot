import requests
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

class AqiCog(commands.Cog):
    AQICN_BASE_URL = 'https://api.waqi.info/feed/'
    load_dotenv()
    AQICN_TOKEN = os.getenv('AQICN_TOKEN')

    def __init__(self, bot):
        self.bot = bot

    @discord.command()
    async def aqi(self, ctx):
        r = requests.get(self.AQICN_BASE_URL + 'Boston/?token=' + self.AQICN_TOKEN)
        if r.status_code == 200:
            r_json = r.json()
            aqi = r_json['data']['aqi']
            await ctx.respond(f'The aqi for Boston: {aqi}')
        else:
            print(f'Error calling AQICN API: {r.status_code}')
            await ctx.respond('Error calling AQICN API')
        # TODO: then get the aqi for other places, also make this more programmatic
    
def setup(bot):
    bot.add_cog(AqiCog(bot))