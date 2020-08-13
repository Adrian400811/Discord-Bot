import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Help(Cog_Extension):
    @commands.command()
    async def help(self, ctx):
        await ctx.send("https://github.com/HK0811/Discord-Bot/wiki/Functions")


def setup(bot):
    bot.add_cog(Help(bot))
