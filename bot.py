import discord
import discord.utils
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import time as t
import json
import asyncio
from aiohttp import ClientSession
import random
import praw
import urllib.parse, urllib.request, re
import aiohttp
import chat_exporter
import io

reddit = praw.Reddit(client_id="ur id", client_secret="ur secret",
                     username="ur username", password="ur pass", user_agent="praw")

token = ('ur token')
prefixes = ['n! ','n!','>', '+', '&', '=']
intents = discord.Intents.default()  # Enable all intents except for members and presences
intents.members = True  # Subscribe to the privileged members intent.
client = commands.Bot(command_prefix=prefixes, intents=intents)

client.remove_command('help')

a = 1


async def status_task():
    while True:
        activity = discord.Activity(name="NightMC", type=discord.ActivityType.watching)
        await client.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(20)
        activity2 = discord.Activity(name="NightMC", type=discord.ActivityType.playing)
        await client.change_presence(status=discord.Status.idle, activity=activity2)
        await asyncio.sleep(20)
        activity3 = discord.Activity(name="NightMC", type=discord.ActivityType.listening)
        await client.change_presence(status=discord.Status.idle, activity=activity3)
        await asyncio.sleep(20)
        activity4 = discord.Activity(name="Under Development", type=discord.ActivityType.playing)
        await client.change_presence(status=
                                     discord.Status.idle, activity=activity4)
        await asyncio.sleep(20)
        activity5 = discord.Activity(name="Donations", type=discord.ActivityType.watching)
        await client.change_presence(status=discord.Status.idle, activity=activity5)
        await asyncio.sleep(20)


@client.event
async def on_member_join(member):
    channel = client.get_channel(803745347385819157)
    if member.guild.id == 803741726829183048:
        embed = discord.Embed(title=f"Welcome to NightMC {member}", description=''':crescent_moon:   NightMC
    
        IP: **Play.Night-mc.tk**
        Port: **19132**
    
        Main Features :
    
        [+] Bedrock and Java **Cross Play** [1.8 - 1.16]
        [+] Lagless 
        [+] [Survival] Vanilla Experience and 4 Other Gamemodes [Anarchy, Plots, Vanilla, Herobrine, and 1 other Coming Soon...]
        [+] BedWars
        [+] SkyWars
        [+] SkyBlock
        [+] Family Friendly Community
        [+] Cool Ranks with Awesome Perks
        [+] Server Cosmetics 
        [+] Many More tons of Features on Discord
        [+] Store
        [+]Memes
        [+]Dope Music
        [+]Active Staff
        [+]Giveaways
        [+]And much more cool stuff. Join our discord below to experience all this. I am sure you won't regret it :D
    
        Thanks For Joining And Please dont Forget to Check our Store at DIscord Here is our Link:
    
        Website Link -> https://www.night-mc.tk/
    
        Forums Link -> https://www.night-mc.tk/forum/
    
        Discord Invite Link -> http://discord.night-mc.tk/
    
        https://discord.gg/nEPNMvBZ5t''', colour=discord.Color.blue())
        embed.set_thumbnail(url='{}'.format(member.avatar_url))
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

        await member.send(embed=embed)
        embed2 = discord.Embed(title=f'Welcome to NightMC {member}', description=''':crescent_moon:   NightMC
    
        IP: **Play.Night-mc.tk**
        Port: **19132**''', colour=discord.Color.blue())
        embed2.set_footer(text="NightMC bot made by TME#7107",
                          icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        embed2.set_thumbnail(url='{}'.format(member.avatar_url))
        rules = client.get_channel(803745354607886376)
        information = client.get_channel(803749955633807401)
        selfroles = client.get_channel(803745360949674054)
        server_ip = client.get_channel(803745947737128961)
        sos = client.get_channel(803769038035484672)
        await channel.send(embed=embed2)
        await channel.send(f'''<:bot:811912806999130142> Hello {member.mention} welcome to NightMC! 
    Please read the {rules.mention} and visit {information.mention} for all you need to know.
    Please go to {selfroles.mention} so you don’t miss out on any important updates.
    You can find all the server ips in {server_ip.mention}, and if you need help at any point please go to {sos.mention} <:bot:811912806999130142>''')
        await member.send(embed=embed)

    else:
        return

@client.event
async def on_member_leave(member):
    channel = client.get_channel(783221061360812032)
    embed = discord.Embed(title="Member Left", description="We are very sorry to see you leave {member}",
                          colour=discord.Color.blue())
    await channel.send(embed=embed)


@client.event
async def on_ready():
    print("The bot is ready")
    client.loop.create_task(status_task())


# Code not working properly will get back to it later
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        embed = discord.Embed(title="Bot mentioned",
                              description="Prefix of the bot as of now is **n! **\n\nPls use **n! help** to view a list of the commands of the bot.",
                              colour=discord.Color.blue())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773049508152999936/786850749916512276/gg.gif")
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await message.channel.send(embed=embed)

    '''cmd_args = message.content.split("]")
    cmd = cmd_args[0]
    if len(cmd_args) > 1:
        title = cmd_args[1]
    if len(cmd_args) > 2:
        description = cmd_args[2]

    if message.content == "n! announce":
        embed = discord.Embed(title=title, description=description, colour=discord.Color.blue())
        embed.set_footer(text="NightMC bot made by TME#7107", icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/783224139800510524/786946157603455006/NGsTdv4V.gif")
        channel = client.get_channel(796713193233580033)
        announce = discord.utils.get(cmd.guild.roles, id=799246006645948467)
        embed2 = discord.Embed(title="Success!!!!", description="Announcement created successfully.",
                               colour=discord.Color.blue())
        embed2.set_footer(text="NightMC bot made by TME#7107",
                          icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await channel.send(embed=embed)
        await channel.send(announce.mention)
        await message.channel.send(embed=embed2)'''

    if "noice" in message.content:
        await message.add_reaction("<:noice:800639390724522004>")

    if "pog" in message.content:
        await message.add_reaction("<:3797_pogchap_bean:801379422187552788>")

    await client.process_commands(message)

    if ":" == message.content[0] and ":" == message.content.lower()[-1]:
        emoji_name = message.content[1:-1]
        for emoji in message.guild.emojis:
            if emoji_name == emoji.name:
                await message.channel.send(str(emoji))
                await message.delete()
                break
            else:
                pass

    if "discord.gg" in message.content.lower():
        owner = [707549304382029845, 471306929575034882, 797453600136888351, 552769094693421056, 765825783687282698]
        if message.author.id in owner:
            return

        else:
            await message.channel.purge(limit=1)
            await message.channel.send(
                f'Hey {message.author.mention} :rage: \nYou are not allowed to post discord links on this server!!!!',
                delete_after=5)

    if "https://discord.gg" in message.content.lower():
        owner = [707549304382029845, 471306929575034882, 797453600136888351, 552769094693421056, 765825783687282698]
        if message.author.id in owner:
            return

        else:
            await message.channel.purge(limit=1)
            await message.channel.send(
                f'Hey {message.author.mention} :rage: \nYou are not allowed to post discord links on this server!!!!',
                delete_after=5)

    if "fuck" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to use bad words on this server because it is a family friendly server...',
            delete_after=5)

    if "shit" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "fucking" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "nigga" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "nigger" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)
    if "niger" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are banned for sending the **n** word on the server!!!',
            delete_after=5)

    if "bitch" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "whore" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "vagina" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "penis" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "testicles" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "holy shit" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "dick" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "pussy" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "gay" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "lesbian" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "shitass" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "sex" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "porn" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "nudes" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)


    else:
        return


@client.event
async def on_reaction_add(reaction, user):
    ChID = '783211257112166412'
    if reaction.message.channel.id != ChID:
        return
    if reaction.emoji == "✅":
        Member = discord.utils.get(user.server.roles, name="Member")
        await client.add_roles(user, Member)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason=None):
    if member == None or member == ctx.message.author:
        embed = discord.Embed(title='BAN WARNING',
                              description=f'Hey {ctx.author.mention},\nYou cannot **ban** urself!!!!',
                              colour=discord.Color.red())
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await ctx.channel.send(embed=embed)
        return

    if reason == None:
        reason = "For not follwing the rules of the server!!!!"
    embed_user = discord.Embed(title="BAN",
                               description=f'Hey {member.mention}, \nYou have been banned on **NightMC** becasuse of\n\n{reason}',
                               colour=discord.Color.blue())
    embed_user.set_footer(text="NightMC bot made by TME#7107",
                          icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await member.send(embed=embed_user)
    embed = discord.Embed(title="BAN Successful",
                          description=f'Hey {ctx.author.mention},\n{member.mention} has been successfully banned from the server',
                          colour=discord.Color.blue())
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await member.guild.ban(member, reason=reason)
    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    member = discord.utils.get(ctx.guild.roles, id=803743837008298044)
    overwrite = ctx.channel.overwrites_for(member)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(member, overwrite=overwrite)
    await ctx.send('Channel locked.')


@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    member = discord.utils.get(ctx.guild.roles, id=803743837008298044)
    overwrite = ctx.channel.overwrites_for(member)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(member, overwrite=overwrite)
    await ctx.send('Channel unlocked.')


@client.command(aliases=['bot_help'])
async def help(ctx):
    embed = discord.Embed(title='HELP', description="Help commands", colour=discord.Color.blue())
    embed.add_field(name="General Commands",
                    value="1. **n! hello** - To know more about the bot.\n2. **n! ping** - To know about the time it takes the bot to respond.\n3. **n! avatar** - To see your profile pic.\n4. **n! avatar <user-name>** Use n! avatar <user-name> where *user-name* is the person whose avatar you want to see.\n5. **n! new** - You can use this command to create a ticket for support.",
                    inline=False)
    embed.add_field(name="Moderator Commands",
                    value="1. **n! delete <no. of messages>** - Use n! delete to delete some messages in a channel. If no number is specified by default it is .\n2. **n! lock** - You can use this command to lock a channel.\n3. **n! unlock** - Use this command to unlock a channel.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/783224073450553344/786625188171219024/MOSHED-2020-12-10-21-36-42.gif")
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await ctx.message.add_reaction("<a:5684_blue_okay:798764126218223656>")
    await ctx.channel.send(embed=embed)


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'sr '
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_leave(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command(aliases=[])
@commands.has_permissions(administrator=True)
async def nick(ctx, member: discord.Member, *, nick):
    if not member:
        member = ctx.member.author
    await member.edit(nick=nick)
    await ctx.send(f'Nickname has been changed to {member.mention}')


@client.command(aliases=['cf'])
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix was **succesfully** changed to **{prefix}**')


@client.command(aliases=['hi', 'Hello', 'sup'])
async def hello(ctx):
    await ctx.send("Hi I am a **bot** made by **TME** using python.")


@client.command()
async def ping(ctx):
    embed = (discord.Embed(
        title="Pong!",
        description=f"The ping is **{round(client.latency * 1000)} ms** or **{client.latency} seconds**.",
        colour=discord.Color.blue()
    ))
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await ctx.channel.send(embed=embed)


'''@client.command()
async def new(ctx, arg1, arg2):
    guild = ctx.message.guild
    if arg1 == "channel":
        await guild.create_text_channel(arg2)

    elif arg1 == "category":
        await ctx.guild.create_category(arg2)'''


@client.command(aliases=['accurate_ping'])
async def exact_ping(ctx):
    await ctx.send(f"The exact ping is **{client.latency * 1000} ms**")


@client.command(aliases=['delete', 'del'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.channel.send(f'{amount} messages deleted by {ctx.message.author}', delete_after=2)


@clear.error
async def func_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        em = discord.Embed(title='Error!!!',
                           description=f'{ctx.author.mention} You do not have permission to execute this command',
                           colour=discord.Color.red())
        await ctx.send(embed=em)


@client.command(aliases=['delete all', 'delete everything'])
@commands.has_permissions(administrator=True)
async def delete_all(ctx, amount=5):
    await ctx.channel.purge(limit=limit)
    await ctx.channel.send(f'{amount} messages deleted by {ctx.message.author}')
    t.sleep(2)
    await ctx.channel.purge(limit=1)


# minecraft commands
@client.command(aliases=['server ip', 'port', 'minecaft ip', 'IP'])
async def ip(ctx):
    embed = discord.Embed(title="IP and Port instructions!!!", description='''The IP and port are given below -

    IP : **play.Night-mc.tk**
    Port : **25904**

    Java users please paste this into the server address : play.night-mc.tk
    Bedrock users please put the ip and port in the respective places. :D

    Also use the command m/ check to see the server status (whether the server is online or not).

    Hope you enjoy your stay :grin:

    Regs,
    The NightMC Team''', colour=discord.Color.blue())
    embed.set_thumbnail(url='https://media.giphy.com/media/TOkOM7ywZC6OI/giphy.gif')
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await ctx.channel.send(embed=embed)


@client.command(pass_context=True, aliases=['j'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel

    voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected:
        await voice.move_to(channel)

    else:
        await channel.connect()

    await ctx.send(f'Joined **{channel}**')


@client.command(pass_context=True, aliases=['l', 'disconnect', 'd'])
async def leave(ctx):
    global voice
    channel = ctx.message.author.voice.channel

    voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected:
        await voice.disconnect()
        await ctx.send(f'Left **{channel}**')

    else:
        await ctx.send(' ERROR: I am not connected to **any** voice channel')


@client.command()
async def invite(ctx):
    global invite
    invite = '**https://discord.com/api/oauth2/authorize?client_id=755322461771530261&permissions=8&scope=bot**'
    await ctx.send("This is the link to **invite** me to your servers \n" + invite)


@client.command()
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author

    show_avatar = discord.Embed(
        title="AVATAR/PROFILE PIC",
        description=f"Here is the **AVATAR/PROFILE PIC** of {member}",
        color=discord.Color.gold()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    show_avatar.set_footer(text="NightMC bot made by TME#7107",
                           icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await ctx.send(embed=show_avatar)


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, *, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1.00

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")

    await ctx.send(file=discord.File(r'song.mp3'))


'''@client.event
async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('There is no such command as of now!')
    if isinstance(error, commands.CheckFailure):
        await ctx.channel.send('You do not have permission to use that command!')'''

WEBHOOK_URL_TEST = "https://discord.com/api/webhooks/800700941157793792/wqzgnUkMeqgNiggGJibBsieF54FqcnzLo2omrVKI-woh97CTf1r3-KWxu0qElb1C4ESG"


@client.command()
async def test(ctx, *, message: str):
    async with ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL_TEST, adapter=discord.AsyncWebhookAdapter(session))
        embed = discord.Embed(title=message)
        await webhook.send(content=message, username=ctx.author.name, avatar_url=ctx.author.avatar_url)


@client.command()
async def test2(ctx):
    await ctx.send("<:8976_ablobunamused:800289912137187328>")


@client.command()
async def test3(ctx):
    embed = discord.Embed(title='HELP', description="Help commands", colour=discord.Color.blue())
    embed.add_field(name="General Commands",
                    value="1. **n! hello** - To know more about the bot.\n2. **n! ping** - To know about the time it takes the bot to respond.\n3. **n! avatar** - To see your profile pic.\n4. **n! avatar <user-name>** Use n! avatar <user-name> where *user-name* is the person whose avatar you want to see.\n5. **n! new** - You can use this command to create a ticket for support.",
                    inline=False)
    embed.add_field(name="Moderator Commands",
                    value="1. **n! delete <no. of messages>** - Use n! delete to delete some messages in a channel. If no number is specified by default it is .\n2. **n! lock** - You can use this command to lock a channel.\n3. **n! unlock** - Use this command to unlock a channel.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/783224073450553344/786625188171219024/MOSHED-2020-12-10-21-36-42.gif")
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

    embed2 = discord.Embed(title="Ticket for support", description="How can we help you :grin:",
                           colour=discord.Color.blue())

    time_up_embed = discord.Embed(title="Session Expired", description='Please use the help command again',
                                  color=discord.Color.red())
    time_up_embed.set_footer(text="NightMC bot made by TME#7107",
                             icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

    contents = [embed, embed2, "This is page 3!", "This is page 4!"]
    pages = 4
    cur_page = 1
    message = await ctx.send(embed=contents[0])
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=20, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page == 1:
                cur_page += 1
                await message.edit(embed=contents[1])
                await message.remove_reaction(reaction, user)


            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=contents[cur_page - 1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.edit(embed=time_up_embed)
            await message.remove_reaction(reaction, client)
            break
            # ending the loop if user doesn't react after x seconds


@client.command()
async def new_help(ctx):
    embed = discord.Embed(title='HELP', description="Help commands", colour=discord.Color.blue())
    embed.add_field(name="General Commands", value="React with <a:2112_wave_animated:798764121771606057>", inline=True)
    embed.add_field(name="Ticket Commands", value="React with :tickets:", inline=True)
    embed.add_field(name="Moderator Commands", value="React with <a:7904_goldbalancehat:798764125378314291>",
                    inline=True)
    embed.add_field(name="Fun commands", value="React with 🤣", inline=True)
    embed.add_field(name="Home Page", value="React with 🏠", inline=True)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/783224073450553344/786625188171219024/MOSHED-2020-12-10-21-36-42.gif")
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

    message = await ctx.send(embed=embed)

    general_command = discord.Embed(title="General Commands",
                                    description="1. **n! hello** - To know more about the bot.\n2. **n! ping** - To know about the time it takes the bot to respond.\n3. **n! avatar** - To see your profile pic.\n4. **n! avatar <user-name>** Use n! avatar <user-name> where *user-name* is the person whose avatar you want to see.\n5. **n! new** - You can use this command to create a ticket for support.",
                                    colour=discord.Color.blue())

    await message.add_reaction("<a:2112_wave_animated:798764121771606057>")
    await message.add_reaction("🎟️")
    await message.add_reaction("<a:7904_goldbalancehat:798764125378314291>")
    await message.add_reaction("🤣")
    await message.add_reaction("🏠")

    time_up_embed = discord.Embed(title="Session Expired", description='Please use the help command again',
                                  color=discord.Color.red())
    time_up_embed.set_footer(text="NightMC bot made by TME#7107",
                             icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["<a:2112_wave_animated:798764121771606057>", "🎟️",
                                                              "<a:7904_goldbalancehat:798764125378314291>", "🤣"]

    page = 0

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=20, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "<a:2112_wave_animated:798764121771606057>" and page != 1:
                page = 1
                await message.edit(embed=general_command)
                await message.remove_reaction(reaction, user)



            elif str(reaction.emoji) == "🏠":
                page = 0
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.edit(embed=time_up_embed)
            await message.remove_reaction(reaction, client)
            break
            # ending the loop if user doesn't react after x seconds

    return


@client.command()
async def new(ctx, *, reason=None):
    if reason == None:
        reason = 'No reason provided'

    category = discord.utils.get(ctx.guild.categories, id=803768724674969611)
    guild = ctx.guild
    member = ctx.author
    staff_role = discord.utils.get(ctx.guild.roles, id=803745332617281576)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        staff_role: discord.PermissionOverwrite(read_messages=True),
    }
    channel = await guild.create_text_channel(f'{member}-Ticket', overwrites=overwrites, category=category)
    await ctx.channel.send(
        f"Ticket created {ctx.message.author.mention}. You can access the ticket here - {channel.mention}")
    await channel.send(f'Hello {ctx.message.author.mention},')
    embed = discord.Embed(title="Ticket for support", description=f"Reason: {reason}\n\nOur staff will be here to help you soon {ctx.author.mention}",
                          colour=discord.Color.blue())

    staff = discord.utils.get(ctx.guild.roles, id=796700508769091635)
    await channel.send(embed=embed)
    transcript_channel = client.get_channel(804714934667313283)
    transcript_embed = discord.Embed(title="Ticket Opened",
                                     description=f'**Opened by**\n{ctx.author.mention}\n\n**Reason**\n{reason}',
                                     colour=discord.Color.green())
    transcript_embed.set_thumbnail(url='https://media.discordapp.net/attachments/804714934667313283/812006759291027556/1f39f.png')
    transcript_embed.set_footer(text="NightMC bot made by TME#7107",
                                icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

    await transcript_channel.send(embed=transcript_embed)


@client.command(pass_context=True, aliases=['gif'])
async def giphy(ctx, *, search=None):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == None:
        embed = discord.Embed(title="ERROR", description='Please provide a gif u would like to search :blush:', colour=discord.Color.red())
        await ctx.message.add_reaction("<:no_icon:803777627521024000>")
    else:
        await ctx.message.add_reaction("✅")
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=ur api&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await ctx.send(embed=embed)

@client.command()
async def oreo(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    search = 'oreo'
    session = aiohttp.ClientSession()
    response = await session.get(
        f'http://api.giphy.com/v1/gifs/search?q=oreo&api_key=ur api&limit=10')
    data = json.loads(await response.text())
    gif_choice = random.randint(0, 9)
    embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
    await ctx.send(embed= embed)

@client.command()
async def save(ctx):
    transcript = await chat_exporter.export(ctx.channel)


    if transcript is None:
        await ctx.send('There is nothing to save XD')

    transcript_file = discord.File(io.BytesIO(transcript.encode()), filename=f"transcript-{ctx.channel.name}.html")
    await ctx.send(file=transcript_file)

@client.command()
async def close(ctx, *, reason=None):
    if reason == None:
        reason = 'No reason provided'
    category1 = discord.utils.get(ctx.guild.categories, id=803768724674969611)
    channel = ctx.message.channel
    if channel.category == category1:
        transcript = await chat_exporter.export(ctx.channel)

        if transcript is None:
            await ctx.send('There is nothing to save XD')

        waiting_embed = discord.Embed(title='Closing Soon', description='Saving Transcript........', colour=discord.Color.blue())
        waiting_embed.set_footer(text="NightMC bot made by TME#7107", icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

        waiting = await ctx.send(embed=waiting_embed)

        transcript_channel = client.get_channel(804714934667313283)
        transcript_file = discord.File(io.BytesIO(transcript.encode()), filename=f"transcript-{ctx.channel.name}.html")
        transcript_embed = discord.Embed(title="Ticket Transcript", description=f'**Closed by**\n{ctx.author.mention}\n\n**Reason**\n{reason}', colour=discord.Color.red())
        transcript_embed.set_footer(text="NightMC bot made by TME#7107", icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await transcript_channel.send(embed=transcript_embed)
        await transcript_channel.send(file=transcript_file)

        embed = discord.Embed(title="Successful", description="Ticket closing in 5 seconds...",
                              colour=discord.Color.blue())
        embed.set_footer(text="NightMC bot made by TME#7107", icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await waiting.edit(embed=embed)
        await asyncio.sleep(5)
        await channel.delete()
    else:
        await ctx.channel.send(
            f"You are not permitted to close this channel as it is not a ticket {ctx.author.mention}")

@client.command()
async def store(ctx):
    embed = discord.Embed(title=":crescent_moon:   NightMC  Store", description='''
    Due to Cross-Play and Bedrock People dont have A UUID So we are not Able to make online Store However We Made our Store On Discord Now So you Guys can get some Awesome ranks with tons of features like cosmetics and 
    permissions like fly, nick, vanish or hide, disguise and Many more! 

    1. **V.I.P** -> This The Cheapest Rank Available and Has Some Basic Perms like /fly, Use only First 3 Cosmetics for Free. Due to Being a Premium Member of the Server, They are Automatically the Part of Beta Tester | Member and Can are  Whitelisted so they can still play. This Rank has a prefix of @V.I.P .

    **Price -> 3 USD**

    2. **V.I.P+** -> This rank being the Second most cheapest rank, it inherits the same features as the V.I.Ps and including the perms to use /disguise, /skin, and can use the first 5 Cosmetics for Free! Its has a Prefix of @V.I.P+.

    **Price -> 5 USD**

''', color=discord.Color.blue())
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(description='''
    3. **M.V.P** -> This Rank is Marked as one of the Most Premium ranks on the Server and has all the Previous features mentioned in the Above rank. This is the Most Highly Recommended Rank and Most Small Youtuber Use it as its a Budget Rank and gives you access to almost everything! Including the Previous features, it has /nick, /kaboom, and some more interesting features including the the perms to access the first 10 Cosmetics for Free! It has a Prefix of @M.V.P.

**Price -> 7.5 USD**

4. **M.V.P+** -> This is the Second most premium rank and can claim Monthly Rewards like coins, experience, and has 10% more chances in winning giveways like store cash or paypal money and also has access to 15 Best cosmetics in the server and also all the Previously mentioned Perms. It has a Prefix of @M.V.P+.

**Price -> 3.5 USD Per Month**

5. **M.V.P++** -> _This Rank is the Most Premium Rank and Has all the Perms a Youtuber Rank would have and Has
access to all Cosmetics and also access to all Cosmetics on the server. They can claim Weekly Rewards and have 25% more chances of winning Giveaways like store cash and all.

**Price -> 5.5 USD Per Month**
''', colour=discord.Color.blue())
    embed.set_image(url="https://cdn.discordapp.com/attachments/786546606127317022/786988979542425621/zJXwJrDd.gif")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/766232569716277249/782142295523852328/759106735389802586.gif")
    await ctx.channel.send(embed=embed)


@client.command()
async def boosters(ctx):
    embed = discord.Embed(title="Booster perks", description='''
1. Bypass All Slowmodes.
2. Exclusive @Server Boosters and @Donators Role.
3. @V.I.P  Role on our Minecraft Server and As well as Discord.
4. Priority Service.
5. 5% Higher Chances of Winning Giveaways!

Note -> Applied for 1 Boost only and Max 2 times also Ranks and Perks will be removed if Unboosted the Server.    
''', color=discord.Color.blue())
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/783224073450553344/786994537830154290/9CGKx4jR.gif")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/766232569716277249/786991725708705822/7552_Pepe_NitroBoost.gif")
    await ctx.channel.send(embed=embed)


@client.command()
async def links(ctx):
    embed = discord.Embed(title="NightMc Links:", description='''

Website Link -> https://www.night-mc.tk/

Forums Link-> https://www.night-mc.tk/forum/

Status Of Server Link -> https://www.night-mc.tk/status/

Staff Applications  Link -> https://www.night-mc.tk/apply/

Permanent Discord Invite Link -> http://discord.night-mc.tk/  
''', color=discord.Color.blue())
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/783224073450553344/786997687018455090/5g5iZhJo.gif")
    embed.set_thumbnail(url="https://discord.com/assets/7c13aa0def6ccb6932f47dedd33f59c1.svg")
    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message: str=None):
    if message == None:
        embed = discord.Embed(title='ERROR!!!', description='Please provide something to announce :blush:', color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    message_args = message.split("  ")
    embed = discord.Embed(title=message_args[0], description=message_args[1], colour=discord.Color.blue())
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/783224139800510524/786946157603455006/NGsTdv4V.gif")
    channel = client.get_channel(803745352742207488)
    announce = discord.utils.get(ctx.guild.roles, id=803745336397004830)
    embed2 = discord.Embed(title="Success!!!!", description="Announcement created successfully.",
                           colour=discord.Color.blue())
    embed2.set_footer(text="NightMC bot made by TME#7107",
                      icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await channel.send(embed=embed)
    #await channel.send(announce.mention)
    await ctx.channel.send(embed=embed2)

@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message: str=None):
    if message == None:
        embed = discord.Embed(title='ERROR!!!', description='Please provide something to say :blush:', color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    message_args = message.split("  ")
    if message_args[1] == None:
        message_args[1] = ' '
    embed = discord.Embed(title=message_args[0], description=message_args[1], colour=discord.Color.blue())
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    embed2 = discord.Embed(title="Success!!!!", description="Announcement created successfully.",
                           colour=discord.Color.blue())
    embed2.set_footer(text="NightMC bot made by TME#7107",
                      icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await ctx.channel.send(embed=embed)



@client.command()
async def partnership(ctx, *, message: str):
    message_args = message.split("  ")
    embed = discord.Embed(title="Partnership", description=message, colour=discord.Color.blue())
    embed.set_footer(text="NightMC bot made by TME#7107",
                     icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/783220975478243358/787247426787868682/fS3WppQl.gif")
    channel = client.get_channel(796718342676545576)
    announce = discord.utils.get(ctx.guild.roles, id=799245937351983124)
    embed2 = discord.Embed(title="Success!!!!", description="Partnership announced succesfully",
                           colour=discord.Color.blue())
    embed2.set_footer(text="NightMC bot made by TME#7107",
                      icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
    await channel.send(embed=embed)
    await channel.send(f'||{message_args[1]}||')
    await channel.send(announce.mention)
    await ctx.channel.send(embed=embed2)


BASE = "https://youtube.com/results"


@client.command()
async def youtube(ctx, *, search):
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


@client.command()
async def report(ctx, member: discord.Member = None, type=None, *, reason=None):
    report_channel = client.get_channel(797314915442229288)
    successful_embed = discord.Embed(title="Report Successful", description='Report created successfully',
                                     colour=discord.Color.green())

    if member == None:
        failed_embed = discord.Embed(title="Report Failed", description="Pls mention someone to report!!!",
                                     color=discord.Color.red())
        await ctx.send(embed=failed_embed)
        return

    elif member != None:
        if type == None:
            failed_embed = discord.Embed(title="Report Failed", description="Please tell a type of report",
                                         color=discord.Color.red())
            await ctx.send(embed=failed_embed)
            return

        elif type != None:
            if reason == None:
                failed_embed = discord.Embed(title="Report Failed",
                                             description="Please mention a valid reason",
                                             color=discord.Color.red())
                await ctx.send(embed=failed_embed)
                return

            elif reason != None:
                types = ['minecraft', 'discord']
                if type.lower() in types:
                    if type.lower() == "minecraft":
                        minecraft_em = discord.Embed(title='Minecraft Report',
                                                     description=f"**Reported user**: {member.mention}\n\n**Reason**: {reason}",
                                                     colour=discord.Color.blue())
                        minecraft_em.set_footer(text=f"Report by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await report_channel.send(embed=minecraft_em)
                        await ctx.channel.send(embed=successful_embed)

                    elif type.content.lower() == "discord":
                        discord_em = discord.Embed(title='Discord Report',
                                                   description=f"**Reported user**: {member.mention}\n\n**Reason**: {reason}",
                                                   colour=discord.Color.blue())
                        discord_em.set_footer(text=f"Report by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await report_channel.send(embed=discord_em)
                        await ctx.channel.send(embed=successful_embed)

                else:
                    failed_embed = discord.Embed(title="Report Failed",
                                                 description="Please tell a valid type of report - minecraft/discord",
                                                 color=discord.Color.red())
                    await ctx.send(embed=failed_embed)
                    return


@client.command()
async def suggest(ctx, *, suggestion: str = None):
    if suggestion == None:
        failed_embed = discord.Embed(title="Suggestion Failed", description="Please tell something to suggest",
                                     color=discord.Color.red())
        await ctx.send(embed=failed_embed)
        return

    embed = discord.Embed(title="Suggestion", description=suggestion, color=discord.Color.blue())
    embed.set_footer(text=f"Suggestion by {ctx.author.name}", icon_url=ctx.author.avatar_url)

    successful_embed = discord.Embed(title="Suggestion Successful", description='Suggestion created successfully',
                                     colour=discord.Color.green())

    channel = client.get_channel(803745358207385620)

    message = await channel.send(embed=embed)

    await message.add_reaction('<a:bot_tick:805658829189677096>')
    await message.add_reaction('<a:cross_bot:805658996773879830>')

    await ctx.send(embed=successful_embed)


# fun commands
@client.command()
async def search(ctx, *, url: str):
    query_string = urllib.parse.urlencode({
        'search_query': url
    })

    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )

    search_results = re.findall('href = watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt',
                 'Yes - definitely',
                 'You may rely on it',
                 'No',
                 'Very doubtful',
                 'Better not tell you now',
                 'Outlook not so good']
    await ctx.channel.send(f'**Question** : {question}\n **Answer** {random.choice(responses)}')


@client.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://www.reddit.com/r/dankmemes/new.json?sort=hot,") as r:
            res = await r.json()
            embed = discord.Embed(title="Meme",
                                  description=f"Fresh Memes  {ctx.author.name}",
                                  colour=discord.Colour.blue()).set_footer(text=f"Requested by {ctx.author.name}",
                                                                           icon_url=ctx.author.avatar_url)
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@client.command()
async def google(ctx, *, search: str = None):
    if search == None:
        search = "bruh u did not search anything -_-"

    search = search.replace(" ", "%20")

    await ctx.send(f"https://www.google.com/search?&q={search}+")


youtube_api_key = 'AIzaSyAHryaoXulySi2TKj0hDe7yiAiMvrFc-Mw'


@client.command()
async def sid(ctx, *, value):
    embed = discord.Embed(title='Sidu Pidu', description=value, color=discord.Color.gold())
    embed.set_image(url='https://cdn.discordapp.com/attachments/783224139800510524/786946157603455006/NGsTdv4V.gif')
    embed.set_footer(text=f'Sid\'s personal command requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="ERROR", description='You do not have permission to execute that command', color=discord.Color.red())
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await ctx.send(embed=embed)

client.run(token)









