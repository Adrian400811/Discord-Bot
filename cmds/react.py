import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
with open('../Discord-Bot/setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if "wau" in msg.content and msg.author != self.bot.user:
            if msg.author.id != 701998387981189191 and msg.author.id != 690221543858503717:
                await msg.channel.send('wau撚夠未')
        if msg.content.endswith('Hi') and msg.author != self.bot.user and msg.author.id != 701998387981189191:
            await msg.channel.send('Hi')
        if msg.content.endswith('hi') and msg.author != self.bot.user and msg.author.id != 701998387981189191:
            await msg.channel.send('hi')


def setup(bot):
    bot.add_cog(React(bot))
