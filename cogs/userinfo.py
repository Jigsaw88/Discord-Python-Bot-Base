import discord
from discord.ext import commands



class userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        embed = discord.Embed(title=f"Userinfo for {member.name}", description=" ", color=0x00ff00)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Ping:', value=member.mention)
        embed.set_footer(text=f"Requeted by {ctx.author}")
        embed.add_field(name="Joined Server", value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'))
        embed.add_field(name="Joined Discord", value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'))
        embed.add_field(name="Status", value=member.status)
        react = await ctx.send(embed=embed)
        await react.add_reaction("😄")

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**ERROR**:\r\n'
                           'Please Tag a member. \r\n'
                           ' ')

def setup(client):
    client.add_cog(userinfo(client))