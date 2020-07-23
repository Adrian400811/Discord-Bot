import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Help(Cog_Extension):
    pass
    #@commands.command()
    #async def help(self, ctx):
        #embed=discord.Embed(title="Help", description="Bot Functions")
        #embed.add_field(name="wau (no prefix)", value='The bot will send "Wau撚夠未"', inline=False)
        #embed.add_field(name="0ping", value="The bot will send the latency between the bot and Discord server", inline=False)
        #embed.add_field(name="0status", value="The bot will send the usage of the CPU, RAM, Disk and GPU of the server", inline=False)
        #await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Help(bot))