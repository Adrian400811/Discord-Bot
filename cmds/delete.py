import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Delete(Cog_Extension):  

    @commands.command(hidden = True)
    async def delete(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        embed=discord.Embed(title="Delete", description=f"Deleted {num} messages", color=0x00ff00)
        embed.set_footer(text="Command Execute Successful")
        await ctx.send(embed=embed)
            

def setup(bot):
    bot.add_cog(Delete(bot))