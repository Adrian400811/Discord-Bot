import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open ("../setting.json", mode='r', encoding='utf8') as sfile:
    sdata = json.load(sfile)

class Say(Cog_Extension):  
    
    @commands.command()
    async def say(self,ctx,*,msg):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            embed=discord.Embed(title="No Private Message", description=f"DM doesn't support this command.", color=0xff0000)
            embed.set_footer(text="err=NoPrivateMessage")
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            await ctx.send(msg)

def setup(bot):
    bot.add_cog(Say(bot))
