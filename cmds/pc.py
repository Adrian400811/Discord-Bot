import psutil
import os
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import datetime
import GPUtil
#from gpiozero import CPUTemperature
from tabulate import tabulate

class pc(Cog_Extension):

    @commands.command()
    async def status(self,ctx):
        cpu = psutil.cpu_percent()
        #ctemp = CPUTemperature()
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        embed=discord.Embed(title="Server Status", color=0x00ff00)
        embed.add_field(name="CPU Usage", value=f"{cpu}%", inline=False)
        #embed.add_field(name="CPU Temperature", value=f"{ctemp.temperature}°C", inline=False)
        embed.add_field(name="RAM Usage", value=f"{mem.percent}%", inline=False)
        embed.add_field(name="Disk Usage", value=f"{disk.percent}%", inline=False)
        embed.set_footer(text="Command Execute Successful")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(pc(bot))