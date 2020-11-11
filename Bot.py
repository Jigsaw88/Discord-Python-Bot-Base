import discord
import asyncio
import aiohttp
from discord.ext import commands, tasks
import os
from itertools import cycle

client = commands.Bot(command_prefix='+', help_command=None)


async def is_owner(ctx):
    return ctx.author.id == 639943536346792017


@client.command()
@commands.check(is_owner)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f"**Module Loaded**", description=f"[{extension}] ✅", color=0x00ff00)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f"**Module Unloaded**", description=f"[{extension}]  ⛔", color=0x00ffff)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_owner)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f"**Module Reloaded**", description=f"[{extension}]  🔄", color=0xff0000)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_owner)
async def showcog(ctx):
    await get_commands()


@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('**You dont have the permission to do that!**')


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('**You dont have the permission to do that!**')


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('**You dont have the permission to do that!**')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print('Bot logged in as: {}'.format(client.user.name))
    client.loop.create_task(status_task())


# @client.event
# async def on_command_error(ctx, error):
#    if isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send('**ERROR**:\r\n'
#                       'You dont have give me all Arguments!')


#@client.event
#async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandError):
#        await ctx.send(f'Hey {ctx.author.mention}. `{error}`')

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Bot by Jigsaw'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(7)
        await client.change_presence(activity=discord.Game('Prefix +'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(15)
        await client.change_presence(activity=discord.Game('Working on the Bot'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(7)
        await client.change_presence(activity=discord.Game(f'on {str(len(client.guilds))} Servers!'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(20)


@client.command()
async def ping(ctx):
    await ctx.send(f'**PONG!**\r\n'
                   f':bar_chart:{round(client.latency * 1000)}ms')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send('{} Messages deleted!'.format(len(deleted)))
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=1)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('User got Kicked!')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'**{member.name} get BANNED!**\r\n'
                   'https://tenor.com/boBQR.gif')


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'User {user.name}#{user.discriminator}')
            return


# status
# @client.command()
# pass
# async def userinfo(ctx, member: discord.Member):
# embed = discord.Embed(title=f"Userinfo for {member.name}", description=" ", color=0x00ff00)
# embed.set_thumbnail(url=member.avatar_url)
# embed.add_field(name='ID:', value=member.id)
# embed.set_footer(text=f"Requeted by {ctx.author}")
# embed.add_field(name="Joined Server", value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'))
# embed.add_field(name="Joined Discord", value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'))
# embed.add_field(name="Status", value=member.status)
# mess = await ctx.send(embed=embed)
# await mess.add_reaction(smile)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**ERROR**:\r\n'
                       'I cant find this Member. \r\n'
                       'Or **YOU** Havent Ping a Member!')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**ERROR**:\r\n'
                       'I cant find this Member. \r\n'
                       'Or **YOU** Havent Ping a Member!')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('```You dont have the permission to do that```')


client.run('TOKEN')
