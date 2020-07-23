import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('../Discord-Bot-0811/setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member}joined!')
        channel = self.bot.get_channel(int(jdata['MAIN_CHANNEL']))
        await channel.send(f'{member} joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member}left!')
        channel = self.bot.get_channel(int(jdata['MAIN_CHANNEL']))
        await channel.send(f'{member} left!')

def setup(bot):
    bot.add_cog(Event(bot))