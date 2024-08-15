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

    # TODO: searching by city name seems highly unreliable, need to figure out consistent search
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

    # get the aqi for some specific areas
    # TODO: consolidate reports into one string. Right now the bot times out before the response is ready
    @discord.command()
    async def aqi_all(self, ctx):
        places = {
            '@5883': 'Boston',
            'A422149': 'Pearl City',
            'A406096': 'Philadelphia',
            'A366688': 'Santa Ana',
            '@5508': 'Seoul',
            'A359320': 'Somerville',
            'A378043': 'Wayne',
            'A475411': 'Yonkers'
        }
        aqi_report = ''
        for station in places.keys():
            r = requests.get(self.AQICN_BASE_URL + f'{station}/?token=' + self.AQICN_TOKEN)
            if r.status_code == 200:
                location = places[station]
                r_json = r.json()
                if r_json['status'] != 'ok':
                    await ctx.respond(f"Cannot retrieve AQI near \"{location}\". \n Error: {r_json['data']}")
                    #aqi_report += f"Cannot retrieve AQI near \"{location}\". \n Error: {r_json['data']}\n"
                else:
                    aqi = r_json['data']['aqi']
                    await ctx.respond(f"The aqi near {location}: {aqi} {self.add_aqi_emojis(aqi)}")
                    #aqi_report += f"The aqi near {location}: {aqi} {self.add_aqi_emojis(aqi)}\n"
            else:
                print(f'Error calling AQICN API: {r.status_code}')
                await ctx.respond('Error calling AQICN API')
        #await ctx.respond(aqi_report)
    
def setup(bot):
    bot.add_cog(AqiCog(bot))