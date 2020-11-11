import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client,):
        self.client = client

    @commands.command()#this replace the org help command!
    async def help(self, ctx):
        embed = discord.Embed(title=" ", description=" ", color=0x00ff00)
        embed.set_author(name="Help", icon_url=ctx.author.avatar_url)
        embed.add_field(name='Welcome to Vault boy!', value='Made by Jigsaw\n\r'
                                                            '-')
        embed.add_field(name='`+help_fun`', value='Show Fun commands\n\r'
                                                  '-')
        embed.set_footer(text=f"Requeted by {ctx.author}   ({ctx.author.id})")
        embed.add_field(name="`+help_Moderation` ", value='Show Moderation Commands\n\r'
                                                          '-')
        embed.add_field(name="`+help_Other`", value='Show Other Commands\n\r'
                                                    '-')


        mess = await ctx.send(embed=embed)







def setup(client):
    client.add_cog(Help(client))
