import discord
from discord.ext import commands
import random
import asyncio
import datetime
client = commands.Bot(command_prefix='+')

class Give(commands.Cog):

    def __init__(self, client):
        self.client = client

    def converts(self, time):
        pos = ["s","m","h","d"]

        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]



    @commands.command()
    @commands.has_role("Giveaway")
    async def gstart(self, ctx, mins: int, *, Prize: str):
        embed = discord.Embed(title="Giveaway!", description=f'{Prize}', color=ctx.author.color)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins * 60)

        embed.add_field(name="Ends at", value=f'{end} UTC')
        embed.set_footer(text=f"Ends {mins} minutes from now!")


        my_msg = await ctx.send(embed=embed)
        await my_msg.add_reaction("🎉")

        await asyncio.sleep(mins)

        new_msg = await ctx.channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()

        winner = random.choice(users)

        await ctx.send(f"{winner.mention} you won {Prize}!")

    @commands.command()
    async def reroll(self, ctx, id_ : int):

        embed = discord.Embed(title="Giveaway!", description=f' ', color=ctx.author.color)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins * 60)

        embed.add_field(name="Ends at", value=f'{end} UTC')
        embed.set_footer(text=f"Ends {mins} minutes from now!")

        channel = discord.TextChannel

        my_msg = await ctx.send(embed=embed)

        new_msg = await ctx.channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()

        winner = random.choice(users)

        await ctx.send(f"The new Winner is:{winner.mention}!")


def setup(client):
    client.add_cog(Give(client))
