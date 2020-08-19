import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Ping(Cog_Extension):  

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Ping", description=f"{round(self.bot.latency*1000)} ms", color=0x00ff00)
        embed.set_footer(text="command execute successful")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))
