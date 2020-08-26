import discord
from discord.ext import commands
import pyqrcode
import png
from pyqrcode import QRCode
from core.classes import Cog_Extension


class QR(Cog_Extension):

    @commands.command()
    async def qr(self, ctx, *, content):
        s = content
        url = pyqrcode.create(s) 
        url.png('qr.png', scale=6)
        await ctx.send(file=discord.File("../Discord-Bot/qr.png"))


def setup(bot):
    bot.add_cog(QR(bot))
