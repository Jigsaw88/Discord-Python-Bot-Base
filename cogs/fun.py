import random
import aiohttp
import discord
import praw
from discord.ext import commands


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        # http://discordpy.readthedocs.io/en/latest/faq.html#what-does-blocking-mean
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                await ctx.send('Here is your Cat :)\n' + res['file'])

    @commands.command()
    async def meme(self, ctx):
        reddit = praw.Reddit(client_id='MrXiSRURehApig',
                             client_secret='3obiSzuwt-m4XWxKiwThFHKeLYvxFw',
                             user_agent='Vault boy')

        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        embed = discord.Embed(title=f"Here is your meme", description=" ", color=0x00ff00)
        embed.set_image(url=submission.url)
        embed.set_footer(text=f"Requeted by {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command()
    async def anime(self, ctx):
        reddit = praw.Reddit(client_id='MrXiSRURehApig',
                             client_secret='3obiSzuwt-m4XWxKiwThFHKeLYvxFw',
                             user_agent='Vault boy')

        Animewallpaper_submissions = reddit.subreddit('Animewallpaper').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in Animewallpaper_submissions if not x.stickied)

        embed = discord.Embed(title=f"Here is your Anime Pic", description=" ", color=0x00ff00)
        embed.set_image(url=submission.url)
        embed.set_footer(text=f"Requeted by {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command()
    async def phcomments(self, ctx):
        reddit = praw.Reddit(client_id='MrXiSRURehApig',
                             client_secret='3obiSzuwt-m4XWxKiwThFHKeLYvxFw',
                             user_agent='Vault boy')

        PornhubComments_submissions = reddit.subreddit('PornhubComments').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in PornhubComments_submissions if not x.stickied)

        embed = discord.Embed(title=f"Here is your Pornhub Comment ;)", description=" ", color=0x00ff00)
        embed.set_image(url=submission.url)
        embed.set_footer(text=f"Requeted by {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command()
    async def Codingmeme(self, ctx):
        reddit = praw.Reddit(client_id='MrXiSRURehApig',
                             client_secret='3obiSzuwt-m4XWxKiwThFHKeLYvxFw',
                             user_agent='Vault boy')

        ProgrammerHumor_submissions = reddit.subreddit('ProgrammerHumor').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in ProgrammerHumor_submissions if not x.stickied)

        embed = discord.Embed(title=f"Here is your Programmer Meme ;)", description=" ", color=0x00ff00)
        embed.set_image(url=submission.url)
        embed.set_footer(text=f"Requeted by {ctx.author}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(fun(client))
