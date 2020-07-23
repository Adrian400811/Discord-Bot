import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Err(Cog_Extension): 
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed=discord.Embed(title="Command not found", description=f"{error}", color=0xff0000)
            embed.set_footer(text="err=command_not_found")
            await ctx.send(embed=embed)
            print(f'{error}')

def setup(bot):
    bot.add_cog(Err(bot))