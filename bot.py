import discord
from discord.ext import commands
from asyncio import *
from discord.emoji import *
from discord.ext import tasks
from itertools import cycle
import bot
from discum.guild import guild
from discum import guild
from discord import channel, guild
from discum.gateway.sessionsettings import guild
from astroid import context
from discord.ext.commands import context
from multiprocessing import context
import random
import aiohttp
import asyncio
import datetime
import re
from spam import spam
import platform
import json
from numpy import number
import time
import json
import discord
import traceback
import secrets
from urllib.request import urlopen
from discord.ext.commands.core import command




class CONFIG:
    TOKEN = 'NzY4Mzk5NzA1NjIxMDA0MzEw.X4_5_Q._jmZsMdf4OIlcauvVlFQM4Hp2wo'
    PREFIX = 'df-'
errors = ['Eshtebah Ast','Khata Dar Neveshtar','Meqdar Eshtebah Vared Kardeid','Lotfan Sahih Vared Konid']
client = commands.Bot(command_prefix=CONFIG.PREFIX)
client.remove_command('help')
GxY = 608619635042025491
Reza = 765884671274778644

@client.event
async def on_ready():
    print('------------------------')
    print("Online")
    print('------------------------')
    bot.statuses = cycle([f'{CONFIG.PREFIX}help', 'Dark Fun Bot','Developers Reza & Mr-GxY'])
    change_status.start()
@tasks.loop(seconds=15)
async def change_status():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name=next(bot.statuses)))
@client.group(invoke_without_command=True)
async def help(ctx):
    funa = client.get_emoji(808647708776071208)
    moda = client.get_emoji(808643470939258890)
    em = discord.Embed(title = "Help", description = "Estefade -help <command> Baraye Fahmidan Kamel Command " , color= 0x979c9f)
    
    em.add_field(name = str(funa)+"Fun"+str(funa) , value = "```Command Haye Sargarmi```")
    
    await ctx.send(embed= em)
@help.command()
async def fun(ctx):
    funa = client.get_emoji(808647708776071208)
    hehe = client.get_emoji(808647473970937887)
    sare = client.get_emoji(809376353786789898)
    em = discord.Embed(title = str(funa)+"Fun", description = "Command Haye Sargarm Konande")

    em.add_field(name = "embeds", value= "Help Embed Ha -help embeds ")
    em.add_field(name = "-say" , value = "-say <Matn>")
    em.add_field(name = "-userinfo", value= "-userinfo <Baraye Gereftan Etelaat Khodeton>")
    em.add_field(name = "-nazarsanji", value= "-nazarsanji <Matn>")
    em.add_field(name = "-timer", value= "-timer <Time>")
    em.add_field(name = "-cat", value= f"Aks Gorbe {str(hehe)}")
    em.add_field(name = "-sarekeyf", value= f"{str(sare)} Sare Keyfi Aziz ?")
    em.add_field(name = "-kill", value= "-kill <@mention>")
    em.add_field(name = "-hi" , value= "Salam Jone Del ")
    em.add_field(name = "-pat" , value= "Naz Kardan Yek Nafar")

    await ctx.send(embed = em)
@help.command()
async def embeds(ctx):
    em = discord.Embed(title = "Send Embed", description = "Command Haye Embed Send")
    
    em.add_field(name = "df-embed" , value= "df-embed <Title> <Description> <Color> <Name> <Value>")
    em.add_field(name = "colors" , value= "gold|green|blue|dark-green|dark-blue|dark-gold")
 

    await ctx.send(embed = em)

@client.command()
async def embed(ctx ,color, title , desc , field , *,value):
    if (color == 'gold'):
        embed=discord.Embed(title=title, description=desc, color=0xc27c0e)
        embed.add_field(name=field, value=value, inline=False)
        await ctx.send(embed=embed)
        await client.get_channel(807357096306933766).send(f"Embed Gold Title **{title}** and description **{desc}** and **{color}** and field **{field}** and value **{value}** ")
    elif (color == 'green'):
        embed=discord.Embed(title=title, description=desc, color=0x2ecc71)
        embed.add_field(name=field, value=value, inline=False)
        await ctx.send(embed=embed)
        await client.get_channel(807357096306933766).send(f"Embed Gold Title **{title}** and description **{desc}** and **{color}** and field **{field}** and value **{value}** ")
    elif (color == 'blue'):
        embed=discord.Embed(title=title, description=desc, color=0x3498db)
        embed.add_field(name=field, value=value, inline=False)
        await ctx.send(embed=embed)
        await client.get_channel(807357096306933766).send(f"Embed Gold Title **{title}** and description **{desc}** and **{color}** and field **{field}** and value **{value}** ")
    elif (color == 'dark-green'):
        embed=discord.Embed(title=title, description=desc, color=0x1f8b4c)
        embed.add_field(name=field, value=value, inline=False)
        await ctx.send(embed=embed)
        await client.get_channel(807357096306933766).send(f"Embed Gold Title **{title}** and description **{desc}** and **{color}** and field **{field}** and value **{value}** ")
    elif (color == 'dark-blue'):
        embed=discord.Embed(title=title, description=desc, color=0x206694)
        embed.add_field(name=field, value=value, inline=False)
        await ctx.send(embed=embed)
        await client.get_channel(807357096306933766).send(f"Embed Gold Title **{title}** and description **{desc}** and **{color}** and field **{field}** and value **{value}** ")
    elif (color == 'dark-gold'):
        embed=discord.Embed(title=title, description=desc, color=0xc27c0e)
        embed.add_field(name=field, value=value, inline=False)
        await ctx.send(embed=embed)
        await client.get_channel(807357096306933766).send(f"Embed Gold Title **{title}** and description **{desc}** and **{color}** and field **{field}** and value **{value}** ")
    else:
        await ctx.send("Shoma Color Ra Eshtebah Vared Kardid ! ")
        await client.get_channel(807357096306933766).send(f"Color Code Is Errored **{color}**")
@client.command()
@commands.has_permissions(administrator=True)
@commands.has_guild_permissions(administrator=True)
async def clear(ctx , vared='100'):
    vared = int(vared)
    pak = await ctx.channel.purge(limit=vared+1)
    await ctx.send(" > " +str(vared) + " Massages Cleared" )
    await ctx.channel.purge(limit=1)


# @client.command()

# async def runme(ctx):
#     if (commands.has_permissions(administrator=True)):
#         await ctx.send("Hello Bitch")
#     elif (commands.has_permissions(administrator=False)):
#         await ctx.send("Bot Dastresi Ersal Nadarad")
#     else:
#         await ctx.send("unkow error")

@client.command()
async def join(ctx):
    await ctx.channel.purge(limit=1)
    name = ctx.author.name
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.voice_client.disconnect()
@client.command()
async def nazarsanji(ctx,*,a):
        accept_decline = await ctx.send(a)
        cross = client.get_emoji(808386167048503296)
        checkM = client.get_emoji(808386178084634672)
        await accept_decline.add_reaction(cross)
        await accept_decline.add_reaction(checkM)
@client.command()
async def say(ctx,*,a,member : discord.Member = None):
    name = ctx.message.author.mention
    tag = ctx.author.discriminator
    await ctx.channel.purge(limit=1)
    await ctx.send(a)
    print("az say estefade shod "+name+"#"+tag+" va goft  "+a)
    await client.get_channel(807357095946747932).send(f"Yek Say Estefade Shod Va Tavasot {name} Va Goft {a} ")
@client.command()
async def userinfo(ctx):
    
    checkM = client.get_emoji(808386178084634672)
    cross = client.get_emoji(808386167048503296)
    name = ctx.author.name
    avatar = ctx.author.avatar_url
    tag = ctx.author.discriminator
    uid = ctx.author.id
    mention = ctx.author.mention
    embed=discord.Embed(title="UserInfo", description="UserName @"+name+"#"+tag, color=0xff0000)
    embed.add_field(name="User Id", value=uid, inline=False)
    await ctx.send(embed=embed)
    await ctx.send("Avatar User => "+str(avatar))
    await ctx.send("Request By => "+str(mention))

@client.command()
async def invite(ctx):
    await ctx.send("Link Invite ==> https://discord.com/api/oauth2/authorize?client_id=768399705621004310&permissions=8&scope=bot")
@client.command()
@commands.has_guild_permissions(administrator=True)
async def lock(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("Channel Lock Shod")
@client.command()
@commands.has_guild_permissions(administrator=True)
async def unlock(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("Channel Unlock Shod")
@client.command(aliases=['javascript', 'nodejs', 'js'])
async def java(ctx):
    # '''Weil Java != Javscript'''
    await ctx.send(':interrobang: Aya Manzoretan javascript ya nodejs bode ?')
    await ctx.send('https://abload.de/img/2016-05-102130191kzpu.png')
@client.command(aliases=['koshtan','marg'])
async def kill(ctx, member:str):
        '''Monty Python'''
        await ctx.send(f'R.I.P. {member}\nhttps://media4.giphy.com/media/l4FGvTL3rGuoo1Oy4/giphy.gif')
@client.command(aliases=['hypu', 'train'])
async def sarekeyf(ctx):
        '''HYPE TRAIN CHOO CHOO'''
        pepehappy = client.get_emoji(808646774289727499)
        hypu = ['https://cdn.discordapp.com/attachments/807357095946747925/809377435904245760/flrcsgwr49y6.png',
                'https://cdn.discordapp.com/attachments/807357095946747925/809377487091924992/22ff93c6-460a-4d56-9816-512531fc42f5.png',
                'https://cdn.discordapp.com/attachments/807357095946747925/809377523313278986/9k.png',
                'https://cdn.discordapp.com/attachments/807357095946747925/809377649948491836/jgg5tnf33t3i.png',
                'https://cdn.discordapp.com/attachments/807357095946747925/809377707020124180/images.png',
                'https://cdn.discordapp.com/attachments/807357095946747925/809378800289710080/9k.png',
                'https://cdn.discordapp.com/attachments/807357095946747925/809378942845845524/Z.png',
                'https://cdn.discordapp.com/attachments/807357095946747925/809378997104279572/Z.png']
        matn = ['Salam Joone Del','Sare Keyfi Aziz ?','Bazam Ye Rooz Jonane Dige','Pasho Alaki Ada Hal Bada Roo Darnayar','Khodaro Shokr','Chetori Joone Del?','Ey Joonam Ey Jaaan']
        msg = f'{pepehappy}  {random.choice(matn)} {random.choice(hypu)}'
        msg2 =await ctx.send(msg)
        await client.get_channel(807357096306933765).send(f"```Sare  Keyf Estefade Shod {msg2}```")
@client.command(aliases=['gorbe'])
async def cat(ctx):
    cats = ['https://i.pinimg.com/originals/c3/2b/fa/c32bfa16bcf864e478d3ddfe32440268.gif',
    'https://media4.giphy.com/media/f8ywYgttpGzzVPH5AO/source.gif',
    'https://i2.wp.com/dianaurban.com/wp-content/uploads/2017/07/01-cat-stretching-feet.gif?resize=500%2C399&ssl=1',
    'https://tenor.com/view/tell-me-more-salem-cat-waiting-gif-5701246',
    'https://i.pinimg.com/originals/62/d1/81/62d1811698581fab04b6767a1398829b.gif',
    'https://tenor.com/view/lazy-cat-stairs-gif-13378074'
    'https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981',
    'https://tenor.com/view/happy-cat-pinch-cute-squishy-gif-4427877',
    'https://tenor.com/view/kitten-cat-typing-typing-cat-gif-5751430'
    ]
    msg = f'Gonah Nadare Ke Gurbe {random.choice(cats)}'
    await ctx.send(msg)
@client.command()
async def time1(ctx):
        '''It's the final countdown'''
        countdown = ['nine','eight','seven','six','five', 'four', 'three', 'two', 'one','zero']
        for num in countdown:
            await ctx.send('**:{0}:**'.format(num))
            await asyncio.sleep(1)
        await ctx.send('**:ok:** Finish Time')
@client.command()
@commands.has_permissions(kick_members=True)
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *reason):
        '''Kickt ein Mitglied mit einer Begründung (MOD ONLY)

        Beispiel:
        -----------

        :kick @Der-Eddy#6508
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.kick(reason=reason)
        else:
            await ctx.send('**:no_entry:** Kasi Ra Vared Nakardid Baraye Kick')
@client.command()
@commands.has_permissions(ban_members = True)
@commands.bot_has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member=None, *reason):
        '''Bannt ein Mitglied mit einer Begründung (MOD ONLY)

        Beispiel:
        -----------

        :ban @Der-Eddy#6508
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.ban(reason=reason)
        else:
            await ctx.send(' > **:no_entry:** Error : Kasi Ra Baraye Kick Entekhab Nakardid')

@client.command()
@commands.has_permissions(ban_members = True)
@commands.bot_has_permissions(ban_members = True)
async def unban(ctx, user: int=None, *reason):
        '''Entbannt ein Mitglied mit einer Begründung (MOD ONLY)
        Es muss die Benutzer-ID angegeben werden, Name + Discriminator reicht nicht

        Beispiel:
        -----------

        :unban 102815825781596160
        '''
        user = discord.User(id=user)
        if user is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await ctx.guild.unban(user, reason=reason)
        else:
            await ctx.send(' > **:no_entry:**Error : Kasi Ra Baraye Unban Entekhab Nakardid!')
@client.command()
@commands.has_permissions(kick_members = True)
@commands.bot_has_permissions(ban_members = True)
async def bans(ctx):
        '''Listet aktuell gebannte User auf (MOD ONLY)'''
        users = await ctx.guild.bans()
        if len(users) > 0:
            msg = f'`{"ID":21}{"Name":25} Begründung\n'
            for entry in users:
                userID = entry.user.id
                userName = str(entry.user)
                if entry.user.bot:
                    username = '🤖' + userName #:robot: emoji
                reason = str(entry.reason) #Could be None
                msg += f'{userID:<21}{userName:25} {reason}\n'
            embed = discord.Embed(color=0xe74c3c) #Red
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Server: {ctx.guild.name}')
            embed.add_field(name='Ranks', value=msg + '`', inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send('**:negative_squared_cross_mark:** Kasi Ban Nashode Ast')
@client.command()
async def dastresi(ctx):
        '''Listet alle Rechte des Bots auf'''
        permissions = ctx.channel.permissions_for(ctx.me)

        embed = discord.Embed(title=':customs:  Permissions', color=0x3498db) #Blue
        embed.add_field(name='Server', value=ctx.guild)
        embed.add_field(name='Channel', value=ctx.channel, inline=False)

        for item, valueBool in permissions:
            if valueBool == True:
                value = ':white_check_mark:'
            else:
                value = ':x:'
            embed.add_field(name=item, value=value)

        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
@client.command()
async def roles(ctx):
        '''Listet die Rollen-Hierarchie des derzeitigen Servers auf'''
        tik = client.get_emoji(808386167048503296)
        msg = f'Role Haye Server {tik} **{ctx.guild}**:\n\n'
        roleDict = {}

        for role in ctx.guild.roles:
            if role.is_default():
                roleDict[role.position] = 'everyone'
            else:
                roleDict[role.position] = role.name

        for role in sorted(roleDict.items(), reverse=True):
            msg += role[1] + '\n'
        await ctx.send(msg)

@client.command(alies=['setrole', 'sr'])
@commands.has_permissions(manage_roles = True)
@commands.bot_has_permissions(manage_roles = True)
async def setrank(ctx, member: discord.Member=None, *rankName: str):
        '''Vergibt einen Rang an einem Benutzer

        Beispiel:
        -----------

        :setrole @Der-Eddy#6508 Member
        '''
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.add_roles(rank)
            await ctx.send(f':white_check_mark: Rolle **{rank.name}** wurde an **{member.name}** verteilt')
        else:
            await ctx.send(':no_entry: Du musst einen Benutzer angeben!')
@client.command(aliases=['wave', 'hi', 'ohaiyo'])
async def hello(ctx):
        '''Nonsense gifs zum Hallo sagen'''
        gifs = ['https://cdn.discordapp.com/attachments/102817255661772800/219512763607678976/large_1.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219512898563735552/large.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518948251664384/WgQWD.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518717426532352/tumblr_lnttzfSUM41qgcvsy.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519191290478592/tumblr_mf76erIF6s1qj96p1o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519729604231168/giphy_3.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519737971867649/63953d32c650703cded875ac601e765778ce90d0_hq.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519738781368321/17201a4342e901e5f1bc2a03ad487219c0434c22_hq.gif']
        msg = f':wave:'
        msg2 = random.choice(gifs)
        await ctx.send(msg)
        await ctx.send(msg2)

@client.command(aliases=['headpat'])
async def pat(ctx, member: discord.Member = None):
        '''/r/headpats Pat Pat Pat :3

        Beispiel:
        -----------

        :pat @Der-Eddy#6508
        '''
        gifs = ['https://gfycat.com/PoisedWindingCaecilian',
                'https://cdn.awwni.me/sou1.jpg',
                'https://i.imgur.com/Nzxa95W.gifv',
                'https://cdn.awwni.me/sk0x.png',
                'https://i.imgur.com/N0UIRkk.png',
                'https://cdn.awwni.me/r915.jpg',
                'https://i.imgur.com/VRViMGf.gifv',
                'https://i.imgur.com/73dNfOk.gifv',
                'https://i.imgur.com/UXAKjRc.jpg',
                'https://i.imgur.com/dzlDuNs.jpg',
                'https://i.imgur.com/hPR7SOt.gif',
                'https://i.imgur.com/IqGRUu4.gif',
                'https://68.media.tumblr.com/f95f14437809dfec8057b2bd525e6b4a/tumblr_omvkl2SzeK1ql0375o1_500.gif',
                'https://i.redd.it/0ffv8i3p1vrz.jpg',
                'http://i.imgur.com/3dzA6OU.png',
                'http://i.imgur.com/vkFKabZ.jpg',
                'https://i.imgur.com/Lb4p20s.jpg',
                'https://cdn.awwni.me/snot.jpg',
                'https://i.imgur.com/5yEOa6u.jpg',
                'https://i.redd.it/dc7oebkfsetz.jpg']

        if member == ctx.me:
            msg = f'Mer30 :D {ctx.author.mention} <:Hiding:322410632517517324> \n{random.choice(gifs)}'
            await ctx.send(msg)
        elif member is not None:
            msg = f'{ctx.author.mention} Shoma Ra Naz Mikonad  {member.mention} :3 \n{random.choice(gifs)}'
            await ctx.send(msg)
        else:
            await ctx.send('Meqdar Vared Nashode =/')

@client.command()
async def timer(ctx, seconds):
    cross = client.get_emoji(808386167048503296)
    checkM = client.get_emoji(808386178084634672)
    try:
        secondint = int(seconds)
        if secondint > 5000000:
            await ctx.send(f" > Moteasefa Az Limit => 5000000 Sanie Bishtar Nemitavanam Hesab Konam !.")
            raise BaseException
        if secondint <= 0:
            await ctx.send(" > Lotfan Addad Bishtar Az 1 Bezarid")
            raise BaseException
        message = await ctx.send(f"**{seconds}**")
        await message.add_reaction(cross)
        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content="Finished")
                break
            await message.edit(content=f"**{secondint}**")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention} Timer Shoma Be Payan Resid {cross}")
    except ValueError:
        await ctx.send(f"Error : Value  Eshtebah Ast ")
@client.command()
async def what(ctx):
        msg = await ctx.send('what =/')
        await asyncio.sleep(2)
        await msg.edit(context='What The Fuck')
def convert(time):
    pos = ["s","m","h","d"]
    time_dict = {"s" : 1,"m" : 60,"h" : 3600 , "d" : 3600*24}
    unit = time[-1]
    if unit not in pos:
        return -1
    try:
        val = int(time[-1])
    except:
        return -2

    return val * time_dict[unit]


@client.command()
@commands.has_role("giveaway")
async def gstart(ctx):
    await ctx.send("Khob 15 Sanie Vaqt Dari Soalat Ra Javab Bedi ")

    questions = ["Dar Kodam Channel Bargozar Shavad ?",
                "Time Ra Moshakhas Konid? [s|m|h|d]",
                "Jayezeye Giveaway Chist?"]
    answers = []
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    for i in questions:
        await ctx.send(i)
        try:
            msg = await client.wait_for('message',timeout =15.0,check = check)
        except asyncio.TimeoutError:
            await ctx.send('Time Shoma Be Payan Resid Va Shoma Soalat Ra Javab  Nadadid')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"Shoma Nemitavanid In Channel Ra Mention Konid{ctx.channel.mention}")
        return 
    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == 1:
        await ctx.send(f"Lotfan Kamel Vared Konid [s|m|h|d")
        return
    elif time == 2:
        await ctx.send("Lotfan Addad Vared Konid Nakalame Mesal 1s")
        return
    
    prize = answers[2]

    await ctx.send(f"Giveaway Dar Channel {channel.mention} Va Be Time {answers[1]} Sakhte Shod")

    embed = discord.Embed(title  = "Giveaway !" , description = f"{prize}" , color = ctx.author.color)

    embed.add_field(name = "Hosted By : " , value= ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now")

    my_msg = await ctx.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Barande Kasi Nist JoOoOoOoOoOoZ {winner.mention} Va Jayeze {prize}")

# sesion 2


@client.command(name="info", aliases=["botinfo"])
async def info(context):
        """
        Get some useful (or not) information about the bot.
        """
        embed = discord.Embed(
            description="Dark Fun Bot",
            color=0x00FF00
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Owner:",
            value="MяヅG×ʏ ᴹᴬᶠᴵᴬ#4544 & Reza#0001",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"{CONFIG.PREFIX}",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.message.author}"
        )
        await context.send(embed=embed)

# bit bit
@client.command(name="bitcoin")
async def bitcoin(context):
        """
        Get the current price of bitcoin.
        """
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: Info",
                description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}",
                color=0x00FF00
            )
            await context.send(embed=embed)
@client.command()
async def jh(ctx , vorodi : str):
    jorats = ['عمیق ترین ترس زندگی ات چیست؟',
    'به نظرت جذاب ترین مرد / زن این جمع چه کسی است ؟',
    'بزرگ ترین حسرت زندگی ات چیست ؟',
    'آیا تا به حال تقلب یا کلاه برداری کرده ای؟ داستانش را تعریف کن',
    'بزرگ ترین دروغ زندگی ات چه بوده است؟',
    ' خجالت آورترین اتفاق زندگی ات را تعریف کن',
    'بدترین کاری که در مقابل چشم مردم انجام داده ای چه بوده است؟',
    'کدام مورد است که بیشتر اطرافیان فکر می کنند درباره تو صحت دارد اما این طور نیست؟',
    'اگر به مدت یک ماه جنس مخالف خود بودی چه کارهایی می کردی؟',
    ' بچه گانه ترین کاری که تا به حال کرده ای چه بوده است؟',
    'اگر می خواستی یک نفر از این جمع را به عنوان عشقت انتخاب کنی چه کسی را انتخاب می کردی؟',
    'احمقانه ترین اعتیاد یا وابستگی که داری چیست؟',
    ' ترسناک ترین خوابی که تا به حال دیده ای چه بوده است؟',
    'شرم آورترین شی موجود در اتاقت چیست؟',
    'آیا تا به حال شکست عشقی خورده ای؟ چه زمانی و چرا؟',
    ' احمقانه ترین کاری که تا به حال کرده ای چه بوده است؟',
    'آیا رازی داری که تا به حال به هیچ کس نگفته باشی؟',
    'نفرت انگیزترین عادت تو چیست؟',
    'آیا این درست است که (هر چیزی که شما یا گروه درباره آن شک دارید را سوال کنید)',
    'به من چیزی بگو که نمی خواهی بدانم',
    'شرم آورترین لحظه زندگی ات کدام لحظه بوده است؟',
    'آیا تا به حال تحقیر شده ای؟ داستانش را تعریف کن',
    ' اگر قرار باشد به مدت یک هفته جایت را با یکی از شرکت کنندگان بازی عوض کنی چه کسی را انتخاب می کنی؟',
    ' کدام کار است که اگر همه پول های دنیا را هم به تو بدهند انجام نمی دهی؟',
    'یکی از رفتارهایت که دوست داری تغییر بدهی چیست؟',
    'بدترین شوخی که با کسی داشته ای چه بوده است؟',
    'اگر نامرئی باشی اولین کاری که انجام می دهی چیست؟',
    'اگر مجبور باشی در یک جزیره به تنهایی با یک نفر زندگی کنی چه کسی را انتخاب می کنی؟',
    'احمقانه ترین حرفی که در لحظات عاشقانه به همسرت زده ای چه بوده است؟',
    'اسم کسی را بگو که وانمود می کنی دوستش داری اما در واقع چشم دیدنش را نداری',
' دردناک ترین تجربه جسمی ات چه بوده است؟',
'اگر غول چراغ جادو داشته باشی سه آرزویت چیست؟',
'احمقانه ترین کاری که مقابل آینه انجام داده ای چه کاری بوده است؟',
'بیشتر از همه به چه کسی حسادت می کنی؟',
 'آیا تا به حال برای همراهی نکردن همسرت در مهمانی یا بیرون رفتن از منزل خودت را به بیماری زده ای؟ چه زمانی بوده است؟',
 'اگر مطمئن باشی هیچ وقت زندانی نمی شوی دوست داری چه کسی را بکشی؟',
'آیا تا به حال درباره سن خود دروغ گفته ای؟',
 'بزرگ ترین ترس تو درباره همسرت چیست؟',
'آیا با دریافت 5 میلیارد تومان حاضر هستی از همسرت جدا شوی؟',
'به کدام عضو بدن خودت علاقه داری و از کدام متنفر هستی؟',
 'اگر بخواهی از این جمع کسی را انتخاب کنی که در یک فیلم نقش همسرت را بازی کند چه کسی است و چرا؟',
 'آخرین باری که گریه کردی چه زمانی بود؟',
 'موردی که بیشتر از همه دوست داری در زندگی ات تغییر دهی چیست؟',
 'بهترین روز زندگی ات چه روزی بوده است؟',
 'ترسناک ترین اتفاقی که برایت افتاده چیست؟',
 'آخرین چیزی که در گوگل سرچ کرده ای چه بوده است؟',
 'از کدام کلمه بیشتر متنفر هستی؟',
 'بهترین دروغی که تا به حال گفته ای چه بوده است؟',
 'خجالت آورترین خاطره کودکی ات چیست؟',
 'اولین باری که به کسی گفتی دوستت دارم چه زمانی و چه کسی بوده است؟',
    ]
    haqiqats = [ 'گونه شرکت کننده سمت راست خود را ببوس',
 'به مدت پنج دقیقه پاهای شرکت کننده سمت چپ خود را ماساژ بده',
 'یک قاشق کره بخور',
 'اولین کلمه ای که به ذهنت می رسد را فریاد بزن',
 'تا زمانی که دوباره نوبت تو شود دراز نشست برو',
 'یک آهنگ را با آواز تا انتها بخوان',
 'با تمام لباس هایی که به تن داری دوش بگیر',
 'به یکی از شرکت کنندگان اجازه بده کلمه ای روی پیشانی ات بنویسد و تا آخر بازی آن را پاک نکن',
 'یک قطعه یخ در شلوار خود قرار بده و صبر کن تا آب شود',
 'ده بار دور خودت بگرد، بعد از آن سعی کن در خط مستقیم راه بروی',
 'یک دقیقه کامل پلک نزن',
 'پنج قاشق از یک چاشنی غذایی بخور',
 'اجازه بده گروه مدل موی جدیدی برایت درست کنند (کوتاه کردن یا درست کردن موها)',
 'زیر بغل شرکت کننده سمت راست خود را بو کن',
 'با آهنگ انتخابی گروه برقص',
 'اجازه بده شرکت کننده ها تو را آرایش کنند (مخصوص پسرها)',
 'آرایشت را پاک کن (مخصوص دخترها)',
 'به مدت یک دقیقه بدون موسیقی برقص',
 'بگذار گروه تو را در وضعیت خنده دار قرار داده و از تو عکس بگیرند',
 'تلفن همراه خود را به یکی از شرکت کنندگان بده تا یک پیام برای هر کسی که در لیست تماس ها است ارسال کند',
 'یک فنجان از معجونی که شرکت کنندگان تهیه کرده اند بنوش (در تهیه معجون نباید از مواد مضر استفاده شود)',
 'کاری کن تا شرکت کننده سمت راستت از خنده روده بر شود',
 'اجازه بده گروه به مدت یک دقیقه به داخل تلفن همراهت سرک بکشند',
 'دست خود را تا آرنج داخل سطل زباله فرو ببر',
 'با دست های خود از یک طرف اتاق به طرف دیگر برو، بهتر است یکی از شرکت کنندگان پاها را بالا نگه دارد',
 'یکی از شرکت کنندگان را انتخاب کن تا به تو سیلی بزند',
 'به مدت سه دقیقه یک حلقه خیالی دور کمر خود بچرخان',
 'کاغذ شکلات را تنها با استفاده از دهان خود باز کن',
 'با هفتمین شماره در تلفن همراه خود تماس گرفته و به مدت 30 ثانیه آهنگی که گروه انتخاب کرده را برایش بخوان',
 'یکی از شرکت کنندگان تو را قلقلک بدهد و سعی کن نخندی',
 'عکس کارت ملی جدیدت را در پروفایل خود قرار بده',
 'گروه یک شی انتخاب می کند تا با آن دندان های خود را مسواک بزنی',
 'نام خود را با زبان روی زمین بنویس',
 'مقداری عسل روی بینی خود مالیده و روی آن را با آرد بپوشان',
 'چشمان خود را ببند و اجازه بده سایر شرکت کنندگان ماده غذایی دلخواهی از یخچال برداشته و داخل دهانت بگذارند',
 'هر شرکت کننده یک کلمه می گوید، تو با آن کلمات یک جمله بساز و در بیوی تلگرام خود قرار بده',
 'کیف، کوله پشتی و کیف پول خود را خالی کن تا سایر شرکت کنندگان ببینند',
 'یک عدد پیاز خام بخور و گریه نکن',
 'جوراب بغل دستی خود را تا پایان بازی مانند دستکش استفاده کن',
 'با چشم های بسته ساندویچ درست کن',
 'برای یک ربع در خیابان راه برو و بلند بلند با خودت صحبت کن',
 'به بالای پشت بام برو و فریاد بزن من بچه سر راهی هستم',
 'درب همسایه بغلی را زده و سوال کن که آیا می توانی هلیکوپتر خود را مقابل خانه آن ها پارک کنی؟',
 'از منزل خارج شده و با حالت سراسیمه از دیگران بپرس آیا تمساح خانگی ات که فرار کرده را ندیده اند؟',
 'با رستوران محل تماس گرفته و بپرس آیا پماد بواسیر دارند؟',
 'از حالا تا آخر بازی مانند یک ربات صحبت کن',
 'بدون استفاده از کلمات آبی و سفید آسمان را توصیف کن',
 'چهار تکه از لباس هایت را با شرکت کننده سمت راستت عوض کن',
 'دندان های شرکت کننده روبرویت را مسواک بزن',
'یک عدد شکلات را روی ترشی بگذار و بخور',
]
    if (vorodi == "jorat"):
        em = discord.Embed(title = "Jorat Va Haqiqat" , description = "**Jorat**" , colro = ctx.author.color)
        em.add_field(name = "**Soal Jorat**" , value = f'**{random.choice(jorats)}**')
        await ctx.send(embed = em)
    elif (vorodi == "haqiqat"):
        em = discord.Embed(title = "Jorat Va Haqiqat" , description = "**Haqiqat**")
        em.add_field(name = "**Soal Haqiqat**" , value = f'**{random.choice(haqiqats)}**')
        await ctx.send(embed = em)
    else:
        await ctx.send(f"{random.choice(errors)} !")
@client.command()
async def mods(ctx):
        """ Check which mods are online on current guild """
        message = ""
        all_status = {
            "online": {"users": [], "emoji": "🟢"},
            "idle": {"users": [], "emoji": "🟡"},
            "dnd": {"users": [], "emoji": "🔴"},
            "offline": {"users": [], "emoji": "⚫"}
        }

        for user in ctx.guild.members:
            user_perm = ctx.channel.permissions_for(user)
            if user_perm.kick_members or user_perm.ban_members:
                if not user.bot:
                    all_status[str(user.status)]["users"].append(f"**{user}**")

        for g in all_status:
            if all_status[g]["users"]:
                message += f"{all_status[g]['emoji']} {', '.join(all_status[g]['users'])}\n"

        await ctx.send(f"Mods in **{ctx.guild.name}**\n{message}")
def date(target, clock=True):
    """ Clock format using datetime.strftime() """
    if not clock:
        return target.strftime("%d %B %Y")
    return target.strftime("%d %B %Y, %H:%M")

@client.command()
async def user(ctx, *, user: discord.Member = None):
        """ Get user information """
        user = user or ctx.author

        show_roles = ', '.join(
            [f"<@&{x.id}>" for x in sorted(user.roles, key=lambda x: x.position, reverse=True) if x.id != ctx.guild.default_role.id]
        ) if len(user.roles) > 1 else 'None'

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=True)
        embed.add_field(name="Account created", value=date(user.created_at), inline=True)
        embed.add_field(name="Joined this server", value=date(user.joined_at), inline=True)
        embed.add_field(name="Roles", value=show_roles, inline=False)

        await ctx.send(content=f"ℹ About **{user.id}**", embed=embed)
@client.command(aliases=['amongus'])
async def imposter(ctx,member : discord.Member = None):
    if (member == None):
        await ctx.send("Lotfan Yek Nafar Ra Mention Konid")
    else:
        imposter1 = [f'''. 　　　。　　　　•　 　ﾟ　　。 　　.
　　　.　　　 　　.　　　　　。　　 。　. 　
.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•
　　ﾟ　　 {member.mention} was not An Impostor.　 。　.
　　'　　　 1 Impostor remains 　 　　。
　　ﾟ　　　.　　　. ,　　　　.　 .``''',
f'''. 　　　。　　　　•　 　ﾟ　　。 　　.
　　　.　　　 　　.　　　　　。　　 。　. 　
.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•
　　ﾟ　　 {member.mention} was An Impostor.　 。　.
　　'　　　 0 Impostor remains 　 　　。
　　ﾟ　　　.　　　. ,　　　　.　 .``'''
]

    await ctx.send(random.choice(imposter1))
@client.command(aliases=['sk'])
async def _shir_or_khat_bezan(ctx):
        '''Flips a coin'''
        choices = ['شما شیر اوردید', 'شما خط اوردید']
        color = discord.Color.green()
        em = discord.Embed(color=color, title='شیر یا خط:', description=random.choice(choices))
        await ctx.send(embed=em)
@client.command()
async def dice(ctx, number=1):
        '''Rolls a certain number of dice'''
        if number > 20:
            number = 20

        fmt = ''
        for i in range(1, number + 1):
            fmt += f'`Dice {i}: {random.randint(1, 6)}`\n'
            color = discord.Color.green()
        em = discord.Embed(color=color, title='Shoma Tas Endakhti', description=fmt)
        await ctx.send(embed=em)
@client.command(aliases=['si', 'server'])
async def serverinfo(ctx):
        '''Get server info'''
        guild = ctx.guild
        guild_age = (ctx.message.created_at - guild.created_at).days
        created_at = f"Server created on {guild.created_at.strftime('%b %d %Y at %H:%M')}. That\'s over {guild_age} days ago!"
        color = discord.Color.green()

        em = discord.Embed(description=created_at, color=color)
        em.add_field(name='Online Members', value=len({m.id for m in guild.members if m.status is not discord.Status.offline}))
        em.add_field(name='Total Members', value=len(guild.members))
        em.add_field(name='Text Channels', value=len(guild.text_channels))
        em.add_field(name='Voice Channels', value=len(guild.voice_channels))
        em.add_field(name='Roles', value=len(guild.roles))
        em.add_field(name='Owner', value=guild.owner)

        em.set_thumbnail(url=None or guild.icon_url)
        em.set_author(name=guild.name, icon_url=None or guild.icon_url)
        await ctx.send(embed=em)
@client.command()
async def shutdown(ctx):
    usid = ctx.author.id
    usname = ctx.message.author.name
    if (usid == GxY) or (usid == Reza):
        await ctx.channel.send("Shutting down...")
        await ctx.channel.send("Bot Is ShutDown")
        await client.logout()
        print(f"Bot Tavasot {usname} Off Shod")
    else:
        await ctx.send("Shoma Admin Bot Nistid")
@client.command(aliases=['hdh'])
async def helpdarhelp(ctx):
    await ctx.send('df-help')
@client.command() 
async def hesab(ctx,amaliat,*nums):
    if (amaliat == '+'):
        operation = " + ".join(nums)
        await ctx.send(f'{operation} = {eval(operation)}')
    elif (amaliat == '-'):
        operation = " - ".join(nums)
        await ctx.send(f'{operation} = {eval(operation)}')
    elif (amaliat == '*'):
        operation = " * ".join(nums)
        await ctx.send(f'{operation} = {eval(operation)}')
    elif (amaliat == '/'):
        operation = " / ".join(nums)
        await ctx.send(f'{operation} = {eval(operation)}')
    else:
        await ctx.send("Amaliat Na Momken")
@client.command()
async def text(ctx,tit , des , name , url , ico , turl , fie , value , footer):
    embed=discord.Embed(title=tit, description=des, color=0xff0000)
    embed.set_author(name=name, url=url, icon_url=ico)
    embed.set_thumbnail(url=turl)
    embed.add_field(name=fie, value=value, inline=False)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
@client.command()
async def skg(ctx , vorodip):
    skgs = ['سنگ','قیچی','کاغذ']
    if (vorodip == 'sang'):
        await ctx.send(random.choice(skgs))
    elif (vorodip== 'kaqaz') or (vorodip == 'kaghaz'):
        await ctx.send(random.choice(skgs))
    elif (vorodip == 'qeichi') or (vorodip == 'gheichi') or (vorodip == 'gheychi'):
        await ctx.send(random.choice(skgs))
    else:
        await ctx.send("Eshtebah Vared Kardid !")
@client.command(name = "Hacker",aliases=["hack"],usage="Fun",description = "Just For Fun")
async def hacker_bi_fanus_in_esm_function_ast(ctx , member : discord.Member = None ):
    tokens = ['YmfRyoGHZfrpkIJKSrsiyp8WRbtK8NWWX2Ble5Q1a5gjEORk39srnod4pwCl','xwzZkX9wuj3YmLLs8DVp65w72ta0ksBHOYwXLuj5DbTNMs5KWRXQKiNCBMrL','gv6bWMj934EuNtNVEgyw651htcL9kKEq5zpQbzN4thn4z0N34bn14e8ogIlo','8ltWGTKD7Uc8YK7VygTmlLoghNAp0UlX3EJAnj3i24gOEbA0ghbrSpvX0TdP','8GNJOsWDrmrpJZal9OqxZDNddkC9xWVvrw25MPw4ZNhyCfHBUXYHrAJsKbr7','QdvAtWDAaRIjB7NKrMXY6CslSdcyEJUlLfJ4ZctZRZ6jUJT9lFVf7drPetdH','QdvAtWDAaRIjB7NKrMXY6CslSdcyEJUlLfJ4ZctZRZ6jUJT9lFVf7drPetdH','zBmPiZ7N61YbXdxk3VxFaljW9pQTsyYMW3i3tvG6arICJgOGWU','N5Q6IFG2FtD3onqgbH2JQiE7ZrFGQhRZHrDPcnOBYaAAlVWRlt','zg8zJ0nf1hbTS7HOActVzBSyzQDJ0u0ol0Kj9tSV2w0MKfvLd9','YvHKeT2HxbzypzG1hfY1E1UToQSKzniALW0Rwdo5vzzszU0Stl','VOpzEZaH1vaYD69UtaheeiAiqcvXfjfmOWei5J0hxWzhNzcJz2','XH66Lc6xVL2C3nIiEHujP6voPZE2rQxgZ9vRq6kltZEoi9APEC','yxlbTvEgJlK2Y0gD9SfT09ojpNeyH9BiLQk4opO5JTpI1UUgSv','slgg1ySNfeGPyKQaMNbdhWgPgj2S0lXltMwV4R3Nlgg2xvC2zf','w3EWOlGqVKJOlAMNDGjAdwfKPXIZ4UOB5odLoW3y1NQKmU7qbG','JSl3KUyJzXl8noLxHklsYQIvsK19G4eAQTiH1sVaccolTD3tYm','p4q0VLPAULFefjPVkU4Sps1jWv3s223Px932p9wQVhcZKHePlk','OJK8UY3tFMWK9imYaczYHw1bqqz8IBuRb6JlMD9lQGXOqANhtd','03XCy4ML6wF5tS7xvCHHzNx5YUpu9t9K7cBFoFiqr94HvfQPeC','EFVCsy4OHRy6AbxS8irzhg1Wr7ZRiApcmPcM9LNU30wOEmhjNf','EzEUF4vgspuCUl1obq8AG3gkMH3kP1PduPynTLjb3DB57QKMrd','CnzDVK83mYomiC1OWcENPTM9eNuVcWkgUXu92Fzr2Jq6m1BR9J','OAyT4yD7101uVtAUOxCa0I5gYMLrhlyTGdqUzEQHNpO4lyt4oB','dFC216U9sE8SG6VPNuDE56x6OM7WRKBXPPDJSXYGxvaUwYKnXo','OopwLO3LxgtvH4PABbe8UcWBwBt0iJAj0FOqJ0t5vzU8kYpCfc',
'MkU8L7qFFPFuniyyLPHd8H4iov0pUsfFUUvN1HnwYqSwvBrrhF',
'jmyipXWXMuIMFKQHrS33UEspuHf69xgEFV6NvmMpc5d16BetZe',
'd32okUJLiMugwcRJW2RZkDb0uaRFiHosfqUGDT9mz9UrUQuL0x',
'KLwTTbkoSb7WgQYqxW9lwMYHCtkvC8CkpdnMP2fW05tAOaycj6',
'nFbwOjybY6eAVtKcV9o2NSCG8aEgpbzKla2aLtRFLrfqhUy08S',
'3ikbDxK8JdeQWqkUaJewqPlRvA84rgAlloIGUydZc7bqbQajR8',
'N1nnu1k7u1SXbhCXdGWY5uHoITUrQw9OGNfPv4DH4MTiAcCMow',
'nKYdrMP9jxlZkqX3i6afbl84uO8Dbl2wJY52xugs61tef9W3aK',
'4vc0nGFoyLLbvWD0ZX417cDg3uBL3Qm7XZYNEENQNpzZfPutdE',
'RG16ZMyIamJOyJjJrAC6EIHVem6ogAZ87i0haobz6rmsc3hclF',
'c9huYs8StVsH8dL3KfNt7Uf4LvJO7kgp0wQtmHJoHTdHJJGpBm',
'NuS0QOS1sv9zpI9kpPw1EKOlTsGTZqNFhdXXy2YQK4Ao0vJZHX',
'1sFMjBqT4jG9IpQezRSBKXiC0GFB9EQPBlDXnavR5i4UhBrjMV',
'9c4z7zB4ZPkiwrAISTt5JM94UryBtNEeA60D8OoE21PC8pp0Bl',
'd8P0Bi6l4FuJhpa0VGWxL96hQ0xf5axHhwfyiaTmGcFPvlsH6z',
'PQ6AO4IZfdD0tgP6myaIkAKKUM730zUMm54wq7CcgcB3fVbG31',
'sgFFbQ7pPisgajEej54Ae4qajAunt1g43H8A8nciyB4TGFZU3m',
'8HeXkVhgV2NAyo1hzvZmM3i4UAF6KkhVQRwdEIHPWHfcklQPE9',
'EaIqxT3mWw8dZKDdqoyVgngBSAvZLh4LJWj04lfoTG8koDZn13',
'i8weyzkVtxDjmipOBqgYHOW2AMhQ1lAuYxjrATUPshDNHVZcrN',
'wSVrosQtcWfNOci1kSzLrxEyoT2o9RHuyfCRcABQmHxNz8nMhk',
'SkY7MdBoEKrYcyx6rHR8gwR7Ps91dAUAA9smT90NR3eYcCJIJ8',
'ZS5pDDBMmI0dYlzIF1Fu4vL71xPYlxrSNjJxiHhvnMIQWycfUO',
'aIBsYGwJ2aZTWRZzZ7g6iT68rCLba06c314ANgcqpXitisbArJ',
'68l7FR6mluf9gaAhUMieJEAq15tvQNtT4Eur4PuOhXXSR0fs9v',
'wHPHEbPjouuXcDl9sTMIkjNdYyzKTKLICLazmFd2ZvOM8p5lFv',
'VKEAsD8TU0EuHnBOemAHc6WPnbZdPayPcFe3v9CRFr4l0RqqVN',
'VB5FL78uJBMcAfV7tW1VIpsyUL6G1RfAzu23xhAaPrnW6R6vrn',
'neLATNiK9Ii20ZnwxKT9gM40OXpoazOsq8EKXgWFiSTn1pp334',
'G7pXImzF7ExL5VsiroswTDqlDMzeSq374ZmJvOUicaEAbTfsp8',
'ECoYrDz58rkM8g9VN4h3bgmgxKO0cpzXycwXwhtGQtjr8LZfLx',
'OrtD5eRy5lSp1KlxeU8PSf8X513ne0bBXsZ2gefEW7DRNYrAKY',
'xdQFFAk42q0Pdcg2BsA85atuj5XH2VTgEbu0m9PajTLH8N0tBd',
'2ppFE4SROYiSB5ywn1djVqvFrDewZ12pij7o3h1pmCQBbMNgRt',
'RIv12XVTmhCnV4SUpqXA4QwZpkxOBGNGJI0IOLZbSfuzeDR02y',
'SsT3MQXKUouZqngQzuP8Sz8WjELCIQVoxS5xaQ9wFjdFc2dLAe',
'DQZsK3KR0Kvepn3oO6pNs3MQcFr48ANn2w9tC9eSN4v7sV1CwX',
'Cz3GAtYTH2Vp9o4OkjzQTrD05oqdkxtOHdOJ12KIMCJ6SnYqza',
'2Vni6z7UQbpHmMkHO3WeKFnZ93gyWX46fUvLo2WslFCbSRE9qE',
'Tjjw6oWg5HMOdu7JeLx5DgmXDBCyFFS6OWBHmGHXTvEg2IzJaa',
'NRB1rrIgzmAx5sFf8GGKynuxcD288JwL2MBjqTDlv7F1ZG9nLD',
'SU0lPM1AvyvRgOtFlUUXd9SC1WS14Ji2sncP9l97dL7tznlreD',
'MSzTIkpjnxKelZ96V9tJJLtykqNrD166Jsdcm0rnvOmtMq9BMj',
'984ZSVKzQuKmqfKiM3FutFRuf6lyN7c8Tj37XAVFuadaFTf7zz',
'w1e1CYmLcrOTP79DSEz2SGusxVznglnOK2nptIrLx8oIUgRtT5',
'PqB2YZGLWAKeoz1093SE5pylzrqIHeTEmlU4tRBQVWQeQLl2jW',
'GNB27LrMwZv9gbAmL6dob78HGJRnIxjmiwDnuW6hh7AfcODzyq',
'GCnspML7VDagnTnmejghOCN0nFqbNoriFShvq0XFPbUWTCTJxr',
'W489u7PPS5sdUkGm1zGWFuMIpyRSG2O5Aa4fil8vG8ZVKuDAvS',
'qk3JYYYl5LXBUXUEgLddFnzWKbnv2sZDYENVK8gjXqN2MFMvM3',
'05szBGHl4Xs9fDPJx8gfRFI8oEsB0FbRoZPVSdKW7qZqpwLgVI',
'bNtnTpOc34yzaU6wwScOkmU5BufeVke4nRYZg6QT8JIqCjEWsj',
'SI1D2660POxGbeb16vOSwFn2oWvGhyi1wZ4YXsL6PL5soSGVbm',
'4nUintsCFi3fAXTQh7Q5NcUx5uDkF32CGZB5erDgbcBZ96cakX',
'Mg4pgb6LlOcGbQWk852GsmfCLduuZXg9W6Ncnj9PzIsn0QKtAY',
'U4PLNHjMXnqG3ICo8eUytb8OVy1QUAdNl0yBarMvAPIFFh9Eh0',
'222pMtpMc2QKXKqXYy8sk01ke0qauZtWT5K1amCcAZVY3Fedh0',
'8g8T5mQGL4PYVPRwmTfnv871siyweMYTiwol7CO139IE81Nfph',
'ywosZ8Rsfb8j4SYfl9R3dUP7XoqYPVC3IFF1uD3H5kkLIKQP4P',
'mHQY8cRKncGEkSKQr1mDjwiErzYRAph88FnDsyeOkkWyZemJ9F',
'8wWhfe5hUEtCnXbfzdW5tdgyibbz2WEF2cgNzvV5tHSEJqEkL6',
'RLYFTyxqEE5CH5xdqePxF3WyDsrRuzEm7ocOvSY7DzJJ4lOTHJ',
'A2L9CjFEHxHaC1f7IsaQtF9mONpUfCYKm5SkvVoBLpq90UxquB',
'LROAHmsS4m4H988QabiLDP2GBop3Jegg7tmC3olDkNC9Kxz7ww',
'nQ68fnuy7y4P5rsZjaH6RbYhKKXLg1kqMXpztu5soQKI1N2OkU',
'csyDZ0WczjT9JtwczOT2LBklJVGfxIqTb6lifM7RNjfQG5tCtu',
'Uz2Lciuv2LIQcxRlg1lXJ8of4iTHir0vi7CSht0wAsWej1tZSk',
'zwqny54uKpg2gpssV7qvIK4pWytMbYYgcjeOtlbqVnjDQHHLTj',
'm5En45DF84EULL05VYZ26IAfmUB37G9NAXxts9lUYSOURwEmCD',
'v4Bg8jOofNjQxD253XbOXiUsEZdY1IwPX4eRNCtFv63pF8UtQO',
'F30ZpBy3v5RoInPqsxTvQiR7gcOYR4UW8zJruotgPQIeVAzqIv',
'Yx9LcoY12hhuxsNAG0CTA0wyRhrS2ECWOUCvPFPK7W7tRZh1Z7',
'YFIq1ZvM3VHB8wXEL3j013Dn3na9xBUFMbB3GPlLh2GcbC0aBT',
'BrTStJbPL0gCGa6Fe3VCIWZrVHa7t5GMKh6A1y0HLrhmdYjLLJ',
'77iL0h3ze1XmJ0xKATtEKle6ICtO08XsVfJjOm1D8jgFNDJLlx',
'ncU9WOaycWJlW00jrzyfofh2CAAG2xvGaeQ0sW7bjC9U3nVQk8',
'18hRfNCcII37eLoFGPDxL17a9UpApijBOydfMY6SXUUcKLpab7',
'W40cOkmyjpN5oQoHnt3XPzXNCQlHjlVtjAW9dn3rO7yka3u9CO',
'c8YI31ce4g9ydbIi1j14zYW1jBYIwvGUXwrouPGQ0eKWakwn83',
'mIm76UffsMuac0BSMwH8aA4JjcmniA9trQcfvk0d4y1TiJbvXs',
'9qlO8T8L4abqaD6Ts7zV54cnxjyvZ3VJh73SdEhROaXFBdgrlW',
'QArjdLDqUlVgr7JReKbFM1YoRMq5YcgQOxpAw5VXXXpFXfoAsO',
'tTJLSyqRj396uD6W1Y40dYTr9FUKojG6HURQ7W0T2bujFfONRY',
'J6UxlwXVC5pUAU3kLuNrLJWkYLflHalSbJ5unAvmeTISzjxuZ2',
'BjbnT432CYlDvfOAgl6GdIwqB0fXaVQ50rb7YuVMCLwRqXKUWO',
'4JBY5i3Z4C8biJS326nKiz9aM1y4PseiRGXJDVg7gQzv9ffM4A',
'y2fWuhmqEO3UOh3jCIyuQmMKeef2nlk3lB8ktRX7gCMAytYO3e',
'm9dUodSaaa9ehy9p2czcDtevPoA9n6mm7b2Qs3sMJYSc91PVCG',
'8xPGEZkn3tuL6XZ5mPgJEC5gTmhFXo7DIQbL6iNySt3zz2jR94',
'0zXyUNLLxpNtc8V0nVNg19kDyP6YOK5jFbgkKFU7OuSUjZgsKp',
'6rwR7x6sti1bGQEejqB2np21kItuOS67HsR2uiSLp4z8Awqm4C',
'jhpW4ykTKq9qOTfDtrz0wuGxLU4Xo3xNoFqa1iqY8ZpFo74HN1',
'DjPGWOTYarx4xRgRJTsQ84cNcPAhEie53xQlNUnFEs9e5WsBMx',
'zrmM4GbBzppGL5Wo0Vf6WiLu83jrdaC7WcpHtMwc30K912MlRX',
'pBHNhIruqwHsmB5sxv63X39NiufiN49Kw86tn86Nvmcogs9OTF',
'aTOo5XnaRia3FtVoD8mMOxZiIMYFPgVmLKoOYZhnQNID3PODal',
'LZz8l2aLMOkI1UXcTrvhKOSZzl7Fdr4KaaNeL5JFCbsbpjb64A',
'zPggOjzQwFvatXfOkbFELS1BGKNzM3KOv15zwmNkQz0XQNsN7H',
'PPh4ppeeWXy954TpdMxKJ9sMaWfaj6Rm8FTHqmClLbt8Mk5N9a',
'ooEWggckLYWfQqeyHiOv4ca1UPMkTS7SOBYRKnlQfpTKUG4imB',
'eT1jkh5XYE9Yk0ddn6QxfXvTr1dGWUJ3rf0yk8b9cXe3LxJJ3a',
'GnqmFSlgBxSrTr23DLNo9ZwmTOw29Pj5X287PzXQv2ItAWVS6f',
'Rr1O0XPLugIozCVI8dGNzxH2aamQVpDhWK3iVMXrGbMXTn5R8z',
'5pxgEPAZ6ZltL9lafuGoWU5yizHsLN8XeXS6is0gR8kBA1L4i2',
'myWFs4nRNcXry6ws3q9rU03OfMSjia9Fen7oefYX9ANo3SapjK',
'6eD7SMKphHYg86i3OSsvqioICvsI81VyO6wVZh0jNoZhvvhOm3',
'kK3CNsvuiulxd5syL9r8s0O26Sh0OrT79EDVPMdHyXXCa51yTH',
'jEV6CoPwGkIZxSGeYwtdFsWi7Obp6snZknvCa8YdOvRC66s5zw',
'sHEunPoMBdcrZrISMWiZdxE0Wr0Tdchgq9xAoiR7b9ooVwVGTG',
'hAMCii1BnB8J6T1Gnco7tZPHlZbvHQzrGy0jiK2v3ZK107ToOT',
'HWRUXlN9mc2ZWSXVTq7fUOB4yiDZ79MhcrIr9cmSHlnisr4kr7',
'lg8KvhIyLtrDIL3oIbHxJd12wqLkm2NDf7xCFUejOl7zY3rmin',
'Vqgimo6aoo37JMUBLKybfZiFAhoCsELBGMPo1NNQcdXsgeEdkP',
'7l0GhhXsIDzcuUQthBzl48W5vVYa3LCl0MpFBPYaIBGdCMrfzx',
'zXURgH30fhKwKZ4J9odK38M7QX5WZmQbnY4CHMFE8RRd8wn6T8',
'CEW4qjvmVRuw5znbmPimOu64mpuREfRFUXu2G6rbVlnC1K93n6',
'nnRS3ft0x8vvY2490NkhmK8FKHfrwThOhR2PP39TCzY2KDSVfE',
'AnIMDd13vowaDCjWyfxukS4f3grvPIFVAMA6yMryJWhzgM01pl',
'dPMxxN2hB9M9y2QqLAosqebNVQCNCdT2yzh9Z2b5WaYn9Cl4rR',
'KxSf3fYPZR0yFQ1TOiCk5Y5Sj57TXIRHAJpEsd2f42jdc7Ll5T',
'fQZMqbrVMx2t27iB15CtWrrUfP20SvxdEbwEoUSWUDHO1LfBSh',
'VpZkisHRrrxHNdYXWFbdinLxLgjEGrR8wJumCC83qJDH7kyAwr',
'R3zF4Td9lH6vEG745k8UVTm6VKLIyciNemPjuVdk2GtiZEQ29n',
'qhNbgY63rmaRSV9MbVwbMZwZP7GW0zNRdbPf326Z8fvRgVHCdi',
'XRkzsysTJXdqEmpWn3SjMr56lfTk3LIyrR7TEFaj7k49Hq49eq',
'U0G2gGmbeayc7YojGckCgBVmmLle1t5YBZyZxTSKwKhE0lIyzJ',
'LkxWT0J64HR6INYU0X6N7L4gVs52ywpf6A5N46S4IrHZzDUDGQ',
'QgZiE07jmJ0d1td1JISOar2ZVwuRzH042CwWLI66hxvNLffjXN',
'sL9WiT8ZJfNY3fW0fDPunf6WaC8UlAbzzoRz4IbQfSc645amo6',
'YGcNdHfMVqgzHXKcuhtp19ZUYlXwJF62D6G3yw77WMoB7Q3RBB',
'wP7NKTi8WgLs5waiBYHJbphqx7AUporWsmJGwcBdrS9jUtNhzv',
'edpfnX7Th9NBKmqq5CzpIA3U5yfBlcQvS06L51rNrz9jd5tVGM',
'qxnCU34dg43QEdjPrxQIKzDdfQHA6AgjikVbktjuJYELAHHIOe',
'YaQWYpUMgKnZRFasujXjQ7mVsOCP8gzZ4b2rcd2A8bpK4hRjSz',
'1eqpJaSczAVVQMh1G7DVzONVW9YasnnW7q9wRSD1FkRewIHW6M',
'4o3MAJdO93MgQXSPEkbBC1Ubv3tGCfrILUdHitktbIrZF9KQ1b',
'2kXl1FcaqOVhbFvlNXvWlG08p0lGFk3A36v3kWfIZdZ0rm2APs',
'6ZNvo3xE803BxlS4bvRi8nZ91oDww169Zfa3p8t24sPN0Jit1G',
'H99nMbMk7I5NdQUjgLjg999NszlpYU5yVRCahecNoAjmOdX8bt',
'EiShDIHqoo883s4fYTMYaGYNaYFZ2ogb8ypMFxEVOnSzMdHOjw',
'Nk7uZfY5If0TmCuwL9J41hs5v112uuxl6Vzz8AerOtU2pVTMBv',
'guLnJYuL89Lahc15lxUXTBe2qxHx3KiEcMul0PmRNbkTQQmhML',
'MhdwyJ8ikYDPHYN73ozm8TZDIkyPXuzM1t6bZCU5wve4giPO6P',
'5lSAat3vrOM5AFmx4ZvJ3GHmrEVZqiF5N0jJvfmlUkT37Hg9Hu',
'w67dxi5oEnxE0YdxMJbaXri80f7DVvZqpgUIYaJPiFMtNboSkw',
'F3xcf9cnXzgu2g5OSXHPlcN0ciiIbluESXBUh22i8oGZUZQLiq',
'ecrXqffq9L20PQRW2skaHgHqDXrPug8eke6cbzfz4A9KhKKkuK',
'8HPgBK2VoCFS1gtrFo1fxKegZuPUc5Owncrmu5H9gFmrB0A8xN',
'h7eeEdBEc7WkbeQHMCWs7VeDzTmScMsgCrwkIZ0okYQ65y1H1B',
'bWjSgC4s6KD7fIba7hKjC52tnlaLPBNFYOpjo3Z6iPWbINHumi',
'db02XG0nYawOhuSVjCYdMxuNeyDpce1I4nnXg1UMzfnqD5GLfS',
'kWy6n2wlzYPCwaGGMaDdw1ZPJ0xVkf4neXOAL7CpBlth3f9aoO',
'S7hYmurpFvZ2DOyKk1ExWL04guWSmlobkaewceVN3VkTmOS4xy',
'prk78umsCJQE4CM47nmPeUbty7ws40k8fYLR8Wq9RrI7sjn638',
'ehjF3ccHHu05OsdpKbQA9a33VK1t76iDYvseXy7VYbY8eDJscT',
'W6qYyRq0xuTA3dg2nYQlmJwCsZbkOKYONcCLr0kIZ36VYk4lLW',
'phO65Le78t8zN3kLbrXlfWNs6sRZPzahDpiqM6CGOtWqBV0Ufp',
'VVJF3fUX7EQxYTumG4igSWd33V7OIXpwL4rJBHCjyas9CYE81j',
'YtwbhH16fphDE33lNSOXroaqzVEzkOf59FXsE4TQfpGntIeAA3',
'TnsWx14uYAGW5m6Mo6F0ptfve3WPXmGTPtqlTaQFfnCDKikgoI',
'qxd4fVr2YqextURrY9B0DfcKygO2wNWS0BekuQL7p5FGxW0mFN',
'L2uk4Hk1xkqGM1Qt4X1dII8k7V8FWCfrwUa7IgXhaTpxnuz4Qw',
'bvxT7ViDjHqDENYHK7HBEMLsZZMkm7XEkYvT5QdtGoHerqrSqr',
'FvcgaR3XFgf70O1SS8ucfiv9xWl1KIGwBzX86BlWJWLbh9x92K',
'aqSAI4pEmYUbdVb60bLUZ41KYreX3SJ14ujg3rSa9qbmD6MjkL',
'J2jMlP1AMFbomijcWnCQ4peBJy1riorhZTkk3t0ZVguQBASXXN',
'fGC1hF2tZh0YwXJtHZ6RJ30LtBVMq3UmLFge7uQTClvKQ2gEAv',
'Ie09QhuHOPeXUjzlBLv6uMc8WKA2YQ55my3iKHYv03BJMlBMlV',
'h9bAeSxUXi3T5UN4pSAMyrLuAXmFmGVsk96edUDbmNbvwREdYH',
'2vXnkXECq6BVWEGNBGN2bqJGbrIztM7lPx2lLEoDE51HrsI6YH',
'lBRbKEEx7AuQT761oSLq9YmDpj0gwVyaZJ60vZFiVdJWG44Cx7',
'54h2DYovNJgRhuqTRYtRf8MP32HK3MmzS472MHYJgwFtEZKI4y',
'oaoOVq4Nzm40DrSHAto6VGMDD3xpaNC9DOyfRChUpE79qB4j3A',
'0aMWQWJ75IZZ2Otbl3wd2gMTewZRktcO3KVhnDTOaTKYN0GjAz',
'zf0WMNp5jm45hdUUC81kMTsXKLQu8y97SGfHIZaTiB1feSJogA',
'NjytiOJSUx7kpy5WKaU1olwxatEhXnKKbgESnT5s4PQuLavytS',
'yIMbZQpc9sQnVrfgcoFi3mbDXP7drT5QdvZFUYCmtJklRA8vld',
'f92eBKPypkPdDy4HD1Nyb0UV5Uu0iwX1bjZ2vGwsHnwXSUgrRO',
'D77wCc0w5V9jGpzLih7VJNuLcl27yS4CWhafuVwbTlieONAF65',
'4KdP7IOfd2McQc0Dfo2oysVXdaCoF7SFRcKZIMvpAGeN6Q2QsC',
'mfHTmnEz5bdTRCA4Pe1ljmMviCJvtsO2bvZ8PIi4GXHAW7DqKO',
'yD0UxEi03MXWRM8wT9AySCq0LTbjgxb7J9dtgWkAt07ebLdSAH',
'T2dtr5V1J3f91u0xttRF7hrfEvC4n9LyIku1oPT3uPDQO8ufI9',
'Z0LsfEp3zkDm1MKRdNb5od3rOdieWlYy2UFzedgXqIsY7553J7',
'HzDLxRpYBpa9i9EeVGISfR4toAASNznQCjq6aqlPhQd8sLfUAU',
'ECjalzEvCppcfPtc1GiJDxLoXDd4tDBfqQ8oYylsHhZlL81Kuy',
'H2WOlpzvQvaDGlPK82wRcKHmZs9kaYUwwMO2Ba3VbQ8cKurEOa',
'KqFlV3cWRf6ssJnU318uzbAJHUfNaYaZYBPdgMhpIwAWdrQJ2O',
'Ix7VsdTasT7pEYkE8kbGocQjenmrRnUI3We2gMkEc07p4BFbg6',
'FQuHyVN9nwS56niSZlG0ysAIzx2gvwaqpircypvpUGy4BW0i9d',
'4mkZBkH34lBhsNZB7KOZnRE7bVLzHrgfMNSYyaW0BGbmTDT6j0',
'L7mN6wjlaqV1slosS6SX7KG3maIoNDciQ7RCo9s6nFKoWVmi6c',
'VInnu4Zj4rXBxU9AUT1ci9FYEu0uw96wtwd2tkqH5XW8SAt3K7',
'LuW69HsfatITvG29HLgEcNWEXpARNjX7vQEZphMHGu2FnyLMUV',
'Aa5I9rd0oNMTbKxpzj3tOjIHTwilPbss3C2KFLQlPEtBvdHTLY',
'8bu1Dxx3dulo6KlBoYJYPdIJcOIWtmKKkFFkbxVTmUk8rnAdWt',
'1JS3BSoKUVbJL3nFidkHKKUtxGekuSXMdpO7B5x5f9HcnpSfHg',
'UYcIbDR4OMtu7xSJERfk7FaT1jGlrGqUEgp5iWhpdEytYkcL6Y',
'iPRNAJSQL9O7MnWo5gHrL5dYKKeU0mbZhTXAdACMQjXUg3R26V',
'UBoQmDjHZSqPE75rspW6QeelC5fg1NuVyc5wirWCE14ZDjjTOJ',
'z2AoTQsXt1ElLrhBQguXq7gloEAm7gC5hquUOAEqusViqIxsFf',
'jw9Ac2zcKHjIXE9DT2etzl6C7drQNRo8a3v56GeNL2TdxHHfpH',
'7ER3QTQX37bqNVnfpoDF1C2n6oH62M9Db2SmGrwqwkBEqrXxfJ',
'I3g8ccU1Yaz5epM9w2axCrPsWmVdVCMveb4w75QK0wawKdVmOv',
'tnCWixugFn3p12V2KKxKayIZY5aC9ECFuYRVfsC2QKXbXNMdqS',
'EXxyxczfGChf0lyZ4bZx6L0ZC32JkqUqVWRgIBq3pr42I28uvN',
'Bidm7dejthqkVX4CKYMnlng1iqw8wizzzKHUT58rGCa6naldkL',
'dS0QRZPLOGDDVOzqVs1KedcP0BZ8WCwr0mG5WzVJegMaUZEYxJ',
'E5Lsy1kx17NSmXoW6ppUziEKlAkzPlmGciagqXu3gJDXMz9a0O',
'fn6JvJmUX9JVOgDHmR6VAXhUGl1GykDdHeSAYJUFhziqs42xWE',
'PSUPNFPgbXYQJTTEnnsvdlK8fxVA3r1ZHWAZNVADopA7IpJw8D',
'q0hLADGeDczxnU1RgR7XcgZi9Wif9V64TEEXEJvJTqdYsAGNgt',
'8ZFDuWwTjCBOnlVitnf96X2cqXclR4tS3T2NWeL6AkiOMDmuwL',
's8SfBYacYzAgKWdHXjxgsLEG8c0KVOpoIHX9U0EgIQiVRGZGk6',
'JuZ3kLhO69dM29iCk5YKEbD4sGHR0vH0FH0i3hsnObRrF4owUd',
'tFFXa7Xw9WqS80xV1Tci99ezrPS1IgdEsan6R9iOKik8XJQA5L',
'gs0VY1SzI9vnabFxMXSbBkePDanA9AhPcxAe4KU6YJyF0xgb4T',
'8EY7tCrWJZsgIvXdabtW1ZThDRdcRwKqMPHNzBmuvtfYxH2MT0',
'xQcCXZXE6VsBQhQLhe6WzS8MOt7zVnpbqPQbcyserjpGi6bdPK',
'aA2nZUTCt3hxUvXkMGFXp5jXwtwLcVB0gUQPuwg7r6kX75db40',
'0Qg06xHX1b0UoL7jPp8K5OJuUdxiqbgPoHrKrWL9bIOSCvWuU2',
'gIWZhyqdcPktgvYaVpT7z1JkiuHOUIWpmm6k6WIaNxweVQ5Fiv',
'52bKy9bEPmvCZKh5SgkHeH8cLatXkKHovnYwRcsu703PVNQ9iw',
'QPfsUKz68BN4iicLzke9gQtTfGkWR7kahniZVltAQuVBXO6gI9',
'Sc3uC0GrzKkDkP4zsjDYdeJe5YutHPmqxLBAw2KJjPhUVaputA',
'oOLpx1GjqH8jQTVpfCiQK751G0Lypejjq02VINrN6vYin9jsqH',
'BTdQpLONZY4410dBN7JsUs88vSVaZGQkziX53brCq64U8gQj8n',
'dgI97oYN4BbBF71VXr0EVXJ9zHmbQNwhRmTFiOW1NoJM0x4hhN',
'039Vxhw0t1w3z01c9ub1beVKYO9Qp7k6rXbbD7wExVNKe6Zdz5',
'Uo8v4vQW91vk7Fs5o4PlUgX9L7czK32pqUclC8RbTQ6zFqeJNN',
'QDsYtLFBaaOq9Vh8BF8bMrAl1P3r4kjLTuK8LtO6osRxotbOm1',
'MW5lxRd95AWIC0wZGJA27d3mCer09PtQue7jIV9klHQ9rLhk30',
'2uhdPiQkUHOd2G40o3pTTXOGosY33tqzDYN2CaaqZNqt2KGfdq',
'wrQJT1hHEIt7ghGlPf0vNGIAWxMFAvmOT2TI7oUrKikKqw73o4',
'7Go3l6h05ggmI0YR5vVoQVX7dFtebF46Ifem5ABgy5JRNaiLRn',
'bErjU2gfGV56Jm6eBizK0UOpC7IHps1TmD9UWgp8fRMGqjNx4M',
'B3h7OuVsswiPwDlJFExPhYXC9MJeO3c8eyzVR827fokx4CYvUf',
'8GwrTXslfhHY0HAKO3VCNUOyybNFoik2LffIPkPoMIeD7lDRHR',
'5NQdXE00UAsrsIEAtYcGVqt62auhi1FCeEHs1GTFspgUDk2I23',
'CjM4f5Xe6X9lCauS2eZk41ibhhyTY1lowiMtTZD07E1pF8SvKx',
'Rdh2INSWOGJTV03Q20hFlsQOcX6HpOVwcYeBWQHozOUT62QrKx',
'YQhzgwvTaqXo0jrZc8cXn9S9idb0WKiQDKTwRO4hbyClnB3ovb',
'PKyfN7w4uepGzFS3cHcmhX1MjS9uI0A3ZUNeJnjkRjhey1LdWq',
'w9csjVy8DNMbLcHXFsBGkoLlLtEQcLy6hS2ILP2pLphua6mNOJ',
'2AcYapJY2fQQK38WuwHlIspC5pjWXBt5NgXJm9tIHoxYe3Qubu',
'7f3mSLuio1zZ3liGBWUDc98waOlZ1csSGe3QVKcNcgLbyWu6Yy',
'PgNOcxzrEMaXeEgiN4oddOpOK4DVg3J5LPSCB0dRif8fwr37Ve',
'fDtJ0tpoXjCfEMF1UG0OwAXYkrwTWghHzF2gtzT4DIWQ6gSnPC',
'P6fjX0P8jn7RIiHJfKwr2HXSgP8b6e1tWhfwHxpga3TFy3yzqa']
    if (member == None):
        await ctx.send("Mikhay Khodeto Hack Koni ! Aln Shoro Mikonam")
        em1 = discord.Embed(title = "Start Hack . . ." , description = f"Id Shoma : {ctx.message.author.id}")
        em1.add_field(name = f"Esmeton : {ctx.message.author.name}" , value = f"Tokeneton : {random.choice(tokens)}")
        em1.set_footer(text="Just For Fun")
        await ctx.send(embed = em1)
    elif (member == ctx.message.author):
        await ctx.send("Khodeto Mention Nakon !")
    else:
        em2 = discord.Embed(title = "Start Hack . . ." , description = f"Id Shakhs Ke Hack Shod : {member.id}")
        em2.add_field(name = f"Esmesh : {member.name}" , value= f"Hack Shode Tavasot : {ctx.message.author.name}")
        em2.add_field(name = "Token Kasi Ke Hack Shod" , value=f"{random.choice(tokens)}")
        em2.set_footer(text="Just For Fun :D")
        await ctx.send(embed = em2)

@client.command()
async def avatar(ctx , member : discord.Member = None):
    mention = ctx.author.mention
    if (member):
        await ctx.send(member.avatar_url)
    else:
        await ctx.send(ctx.message.author.avatar_url)
@client.command()
async def rt(ctx , vorodi1 , vorodi2 ):
    if (vorodi1 == 'yellow'):
        await ctx.send(f'''```css
{vorodi2}
        ```''')
    elif (vorodi1 == 'blue'):
        await ctx.send(f'''```css
        .{vorodi2}
        ```''')
    elif (vorodi1 == 'green'):
        await ctx.send(f'''```yml
        {vorodi2}
        ```''')
    else:
        await ctx.send("Color Unkow")
client.run(CONFIG.TOKEN)