import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

class Wau(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith('wau'):
            await msg.channel.send('wau撚夠未')

def setup(bot):
    bot.add_cog(Wau(bot))
