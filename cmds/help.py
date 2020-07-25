import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Help(Cog_Extension):
    #@commands.command()
    #async def help(self, ctx):
        #embed=discord.Embed(title="Help", description="Bot Functions")
        #embed.add_field(name="wau *no prefix*", value='The bot will send "Wau撚夠未"', inline=False)
        #embed.add_field(name="ping", value="The bot will send the latency between the bot and Discord server", inline=False)
        #embed.add_field(name="status", value="The bot will send the usage of the CPU, RAM, Disk and GPU of the server", inline=False)
        #embed.add_field(name="qr (content)", value="The bot will generate a QR Code", inline=False)
        #embed.add_field(name="avatar (mention a person)", value="The bot will send the avatar of the person", inline=False)
        #embed.add_field(name="say (message)", value="The bot will copy what you say", inline=False)
        #embed.add_field(name="Hi/hi *no prefix*", value="The bot will also say Hi/hi to you", inline=False)
        #await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self,ctx,*cog):
        """Gets all cogs and commands of mine."""
        try:
            if not cog:
                """Cog listing.  What more?"""
                halp=discord.Embed(title='Cog Listing and Uncatergorized Commands',
                                   description='Use `!help *cog*` to find out more about them!\n(BTW, the Cog Name Must Be in Title Case, Just Like this Sentence.)')
                cogs_desc = ''
                for x in self.bot.cogs:
                    cogs_desc += ('{} - {}'.format(x,self.bot.cogs[x].__doc__)+'\n')
                halp.add_field(name='Cogs',value=cogs_desc[0:len(cogs_desc)-1],inline=False)
                cmds_desc = ''
                for y in self.bot.walk_commands():
                    if not y.cog_name and not y.hidden:
                        cmds_desc += ('{} - {}'.format(y.name,y.help)+'\n')
                halp.add_field(name='Uncatergorized Commands',value=cmds_desc[0:len(cmds_desc)-1],inline=False)
                await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('',embed=halp)
            else:
                """Helps me remind you if you pass too many args."""
                if len(cog) > 1:
                    halp = discord.Embed(title='Error!',description='That is way too many cogs!',color=discord.Color.red())
                    await ctx.message.author.send('',embed=halp)
                else:
                    """Command listing within a cog."""
                    found = False
                    for x in self.bot.cogs:
                        for y in cog:
                            if x == y:
                                halp=discord.Embed(title=cog[0]+' Command Listing',description=self.bot.cogs[cog[0]].__doc__)
                                for c in self.bot.get_cog(y).get_commands():
                                    if not c.hidden:
                                        halp.add_field(name=c.name,value=c.help,inline=False)
                                found = True
                    if not found:
                        """Reminds you if that cog doesn't exist."""
                        halp = discord.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=discord.Color.red())
                    else:
                        await ctx.message.add_reaction(emoji='✉')
                    await ctx.message.author.send('',embed=halp)
        except:
            await ctx.send("Excuse me, I can't send embeds.")
        
def setup(bot):
    bot.add_cog(Help(bot))