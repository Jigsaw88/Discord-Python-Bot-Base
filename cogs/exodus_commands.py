import discord
from discord.ext import commands


class exodus_commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ehelp(self, ctx):
        embed = discord.Embed(title=f"Exodus Sprx by Kushdevv and Rainz Modz", description=" ", color=0x00ff00)
        embed.add_field(name=f'``+edownload``', value='Give you the Download link')

        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(exodus_commands(client))
