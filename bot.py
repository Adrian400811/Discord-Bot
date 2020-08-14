# import modules
import discord
from discord.ext import commands
import json
import os
import datetime
import asyncio
import tasks

# open json file
with open('../Discord-Bot/setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# define prefix
bot = commands.Bot(command_prefix='4', help_command=None)

async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('type "4help" for help!'))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("python version: 3.8"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("discord.py version: 1.3.4"))
        await asyncio.sleep(10)

# send msg on ready
@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    date_time = datetime.datetime.now()
    time = date_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO] System Time: {time}")
    print(f"[INFO] Logged in as {bot.user}")
    print(">>Bot is online<<")


@bot.group(hidden=True)
async def extension(ctx):
    pass

# command: load
@extension.command(hidden=True)
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension}')


# command: unload
@extension.command(hidden=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension}')


# command: reload
@extension.command(hidden=True)
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension}')


for filename in os.listdir('../Discord-Bot/cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

# let the bot run
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
