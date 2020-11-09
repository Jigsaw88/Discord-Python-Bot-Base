import discord
from discord.ext import commands
from discord import User

class command_loader(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def is_owner(ctx):
        return ctx.author.id == 639943536346792017

    async def ping_ghost(ctx):
        return ctx.author.id == 639943536346792017

    @commands.command()
    @commands.check(ping_ghost)
    async def ghostping(self, ctx, member: discord.Member):
       await ctx.send(f'{member.mention}')
       await ctx.channel.purge(limit=2)

    @ghostping.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('```You dont have the permission to do that```')

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title=f"Invite me to your Server!", description="https://bit.ly/3n7bO2x", color=0xa200ff)
        embed.set_image(url="https://cdn.discordapp.com/attachments/642066041362579466/774738336345882684/7536096ef7b07e6a5a30ca6bea03e348.jpg")
        embed.set_footer(text=f"Requeted by {ctx.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def av(self, ctx, member: discord.Member):
        embed = discord.Embed(title=f"Avatar from {member}", description=" ", color=0xa200ff)
        embed.set_image(url=f"{member.avatar_url}")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(command_loader(client))
