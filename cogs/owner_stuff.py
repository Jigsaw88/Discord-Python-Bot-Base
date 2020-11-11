import discord
from discord.ext import commands
import sys
import asyncio


class owner_stuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def is_dev(ctx):
        return ctx.author.id == 639943536346792017

    @commands.command()
    @commands.check(is_dev)
    async def restart(self, ctx):#ik this dont work! fix it by yourself or wait for a update!
        await ctx.send('```RESTART STARTING```')
        await self.client.logout()
        await asyncio.sleep(10)
        await self.client.connect()
        await ctx.send(f'{ctx.author.mention} ```Restart Finished!```')

    @commands.command()
    @commands.check(is_dev)
    async def off(self, ctx):
        await ctx.send(f'{ctx.author.mention} System is shutting down now!')
        await self.client.logout()

    @off.error
    async def off_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send('```Stopped! You are not the owner of the bot```')

def setup(client):
    client.add_cog(owner_stuff(client))
