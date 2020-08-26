import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Help(Cog_Extension):
    @commands.command()
    async def help(self, ctx):
        await ctx.send("https://hk0811.github.io/Discord-Bot/functions.html")

    @commands.command()
    async def dev(self, ctx):
        await ctx.send("https://hk0811.github.io/HK0811/")


def setup(bot):
    bot.add_cog(Help(bot))
