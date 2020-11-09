import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client,):
        self.client = client

    @commands.command()
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

    @commands.command()
    async def help_fun(self, ctx):
        embed = discord.Embed(title=" ", description=" ", color=0x00ff00)
        embed.set_author(name="Help fun")
        embed.add_field(name='Help commands :smile:', value='-')
        embed.add_field(name="`+meme` ", value='Give you random Meme\n\r'
                                               '-')
        embed.add_field(name='`+anime`', value='Give you a random Anime Picture\n\r'
                                               '-')
        embed.set_footer(text=f"Requeted by {ctx.author}   ({ctx.author.id})")
        embed.add_field(name="`+phcomments` ", value='Give you random funny PH Comments\n\r'
                                                     '-')
        embed.add_field(name="`+codingmeme`", value='Give you a random Coding meme\n\r'
                                                    '-')
        embed.add_field(name="`+av [User]`", value='Give you the Avatar of the User\n\r'
                                                   '-')
        await ctx.send(embed=embed)

    @commands.command()
    async def help_moderation(self, ctx):
        embed = discord.Embed(title=" ", description=" ", color=0x00ff00)
        embed.set_author(name="Help Moderation", icon_url=':smile:')
        embed.add_field(name='Help commands :smile:', value='-')
        embed.add_field(name="`+ban [User]` ", value='Ban the pinged Member\n\r'
                                                     '')
        embed.add_field(name='`+kick [User]`', value='Kick the pinged Member\n\r'
                                                     '-')
        embed.set_footer(text=f"Requeted by {ctx.author}   ({ctx.author.id})")
        embed.add_field(name="`+clear [Amount]`", value='Clear Messages\n\r'
                                                        '-')
        await ctx.send(embed=embed)

    @commands.command()
    async def help_other(self, ctx):
        embed = discord.Embed(title=" ", description=" ", color=0x00ff00)
        embed.set_author(name="Help other", icon_url=':smile:')
        embed.add_field(name='Help commands :smile:', value='.')
        embed.add_field(name="`+userinfo [User]` ", value='Give you a Userinfo for the tagged member')
        embed.set_footer(text=f"Requeted by {ctx.author}   ({ctx.author.id})")
        await ctx.send(embed=embed)






def setup(client):
    client.add_cog(Help(client))
