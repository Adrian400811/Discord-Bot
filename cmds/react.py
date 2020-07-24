import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
with open('../Discord-Bot/setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if "wau" in msg.content and msg.author != self.bot.user and msg.author.id != 701998387981189191:
            await msg.channel.send('wau撚夠未')
        if msg.content.endswith('Hi') and msg.author != self.bot.user and msg.author.id != 701998387981189191:
            await msg.channel.send('Hi')
        if msg.content.endswith('hi') and msg.author != self.bot.user and msg.author.id != 701998387981189191:
            await msg.channel.send('hi')

    @commands.group()
    async def question(self, ctx):
        await ctx.send("Answer:")

    @question.command()
    async def program_language(self, ctx):
        await ctx.send("Python 3.8")

    @question.command()
    async def coding_program(self, ctx):
        await ctx.send("Visual Studio Code (VS Code)")

    @question.command()
    async def server(self, ctx):
        await ctx.send("HP Pavilion Power Laptop 15-cb014 with Ubuntu 20.04")

def setup(bot):
    bot.add_cog(React(bot))