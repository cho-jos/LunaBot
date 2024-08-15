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

    def add_aqi_emojis(self, aqi):
        if 0 <= aqi <= 50:
            return ':green_circle: Good'
        elif 51 <= aqi <= 100:
            return ':yellow_circle: Moderate'
        elif 101 <= aqi <= 150:
            return ':orange_circle: Unhealthy for sensitive groups'
        elif 151 <= aqi <= 200:
            return ':red_circle: Unhealthy'
        elif 201 <= aqi <= 300:
            return ':purple_circle: Very Unhealthy'
        elif aqi > 300:
            return ':rotating_light: HARZARDOUS!'

    # TODO: then get the aqi for other places, also make this more programmatic
    @discord.command()
    async def aqi(self, ctx, arg):
        r = requests.get(self.AQICN_BASE_URL + f"{arg}/?token=" + self.AQICN_TOKEN)
        if r.status_code == 200:
            r_json = r.json()
            if r_json['status'] != 'ok':
                await ctx.respond(f"Cannot retrieve AQI for \"{arg}\". \n Error: {r_json['data']}")
            else:
                aqi = r_json['data']['aqi']
                await ctx.respond(f"The aqi for {arg}: {aqi} {self.add_aqi_emojis(aqi)}")
        else:
            print(f'Error calling AQICN API: {r.status_code}')
            await ctx.respond('Error calling AQICN API')
    
def setup(bot):
    bot.add_cog(AqiCog(bot))