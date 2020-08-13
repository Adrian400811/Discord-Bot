import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Avatar(Cog_Extension):
    @commands.command()
    async def avatar(self, ctx, *, avamember: discord.Member = None):
        avaurl = avamember.avatar_url
        await ctx.send(avaurl)


def setup(bot):
    bot.add_cog(Avatar(bot))
