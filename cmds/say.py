# import modules
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

# open json file
with open("../Discord-Bot/settings.json", mode='r', encoding='utf8') as sfile:
    sdata = json.load(sfile)


# build a class
class Say(Cog_Extension):

    # command: say
    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    # command: sayt
    @commands.command()
    async def sayt(self, ctx, *, msg):
        channel = self.bot.get_channel(int(sdata['MAIN_CHANNEL']))
        await channel.send(msg)
        await ctx.send("sent")


# setup
def setup(bot):
    bot.add_cog(Say(bot))
