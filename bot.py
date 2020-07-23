#import modules
import discord
from discord.ext import commands
import json
import os
import datetime

#open json file
with open('../Discord-Bot/setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

#define prefix
bot = commands.Bot(command_prefix='4')

#send msg on ready
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Running on Ubuntu 20.02 LTS"))
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(">>Bot is online<<")

@bot.group()
async def extension(ctx):
    pass

#command: load
@extension.command(hidden=True)
async def load (ctx, extension):
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension}')

#command: unload
@extension.command(hidden=True)
async def unload (ctx, extension):
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'unloaded {extension}')

#command: reload
@extension.command(hidden=True)
async def reload (ctx, extension):
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'reloaded {extension}')


for filename in os.listdir('../Discord-Bot/cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

#let the bot run
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
