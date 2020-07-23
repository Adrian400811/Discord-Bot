import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('../Discord-Bot/setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Saytest(Cog_Extension): 
  @commands.command(hidden=True)
  async def sayt(self,ctx,*,msg):
      channel = self.bot.get_channel(int(jdata['MAIN_CHANNEL']))
      await channel.send(msg)
    
def setup(bot):
    bot.add_cog(Saytest(bot))
