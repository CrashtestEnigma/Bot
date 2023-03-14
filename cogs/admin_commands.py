import discord
import random
import os
import asyncio
import datetime
import pytz
from discord.ext import commands
from time import sleep
intents = discord.Intents.all()
intents.members = True

class Mod(commands.Cog):
    def __init__(self,client):
        self.bot=client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def Spam(self,ctx, member: discord.Member, time=1, amount=1, *, args=None):
        for j in range(amount):
            channel = await member.create_dm()
            await channel.send(args)
            sleep(time)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def dm(self,ctx, member: discord.Member, *, args=None):
        await member.send(args)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clean(self,ctx, amount:int):
      if amount>25:
        await ctx.message.reply('> Make sure to enter a number less than 25!')
        return
      else:
        await ctx.channel.purge(limit=amount)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def nick(self,ctx, member: discord.Member, *, nick):
        await member.edit(nick=nick)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        logs=self.bot.get_channel(838363695036891147)
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.datetime.now(IST)
        modrole = discord.utils.get(guild.roles, name='Mod')
        embedlog=discord.Embed(title=f'{str(member.name)} has been banned.',description=f'Reason : {reason}',color=discord.Colour.blue(),timestamp=datetime.datetime.utcnow())
        embedlog.set_author(name=f'{member.name} has been banned!',icon_url=member.avatar_url)
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_footer(text=f" Reason: {reason}")
        embed.set_author(name=str(member.name), icon_url=member.avatar_url)
        list = [
            'https://images-ext-1.discordapp.net/external/_7IOpr1S3ULIcPCZypYxqnZm1OPtC_Yy_CiEjbAnjqA/https/media.discordapp.net/attachments/446525801920331776/571517154911059978/BANNED_RWBY.gif',
            'https://media.giphy.com/media/dvOwFmfbzmAsI9v2IV/giphy.gif']
        embed.set_image(url=random.choice(list))

        if member.mention == ctx.author.mention:
            await ctx.send('You cannot ban yourself.')
        elif modrole in member.roles:
            return
        else:
            await ctx.send(embed=embed)
            await member.send(f" You have been banned from {guild.name}")
            await logs.send(embed=embedlog)
            await member.ban(reason=reason)

        
        

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        logs = self.bot.get_channel(838363695036891147)
        modrole = discord.utils.get(guild.roles, name='Mod')
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(name=f'{member.name} has been kicked!', icon_url=member.avatar_url)
        embed.set_footer(text=f'Reason: {reason}')
        embedlog=discord.Embed(description=f'Reason: {reason}', color = discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embedlog.set_author(name=f'{member.name} has been kicked!')
        embedlog.set_thumbnail(url=member.avatar_url)
        if member.mention == ctx.author.mention:
            await ctx.send('You cannot kick yourself.')
        elif reason == None:
            await ctx.send('Be more specefic!')
        elif modrole in member.roles:
            return
        else:
            await ctx.send(embed=embed)
            await logs.send(embed=embedlog)
            await member.send(f" You have been kicked from {guild.name}")
            await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unban(self,ctx, *, member):
        logs = self.bot.get_channel(838363695036891147)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        embed=discord.Embed(title=f'{member.name} has been unbanned.', colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await logs.send(embed=embed)
                await ctx.guild.unban(user)
                await ctx.send(f" **{user.name}#{user.discriminator} has been unbanned! **")
                return

                

    @commands.command(aliases=['Mute , m , M'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx, members: discord.Member, mute_time= None, reason=None):
      mute_time = mute_time.lower()
      muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
      if members is None:
        pass
      else:
        for m in members:
          m.add_roles(muted_role)


        num_list = [int(i) for i in mute_time.split() if i.isdigit()]
        str_list = [int(i) for i in mute_time.split() if not i.isdigit()]
        mute_num = ''
        mute_for = ''
        for e in num_list:
          mute_num += e
        for e in str_list:
          mute_for += e

        mute_for = mute_for.lower()

        embed = discord.Embed(
        title=f'{members} have been muted.',
        color= discord.Color.green()
        )
        await embed.add_field(name='Reason: ', value=reason)

        embed2 = discord.Embed(
        title=f'{members} has been muted.',
        color= discord.Color.green()
        )
        await embed2.add_field(name='Reason: ', value=reason)


        
        if mute_for == 'sec' or mute_for == 'secs' or mute_for == 'second' or mute_for == 'seconds':
          complete_time = str(mute_time)+mute_for
          await embed.add_field(name='Muted for: ', value=complete_time)
          if len(members) == 1:
            await ctx.send(embed2)
          else:
            await ctx.send(embed)

          await asyncio.sleep(mute_num)

          for m in members:
            m.remove_roles(muted_role)

        if mute_for == 'hour' or mute_for == 'hours' or mute_for == 'hr' or mute_for == 'hrs':
          complete_time = str(mute_time)+mute_for
          await embed.add_field(name='Muted for: ', value=complete_time)
          if len(members) == 1:
            await ctx.send(embed2)
          else:
            await ctx.send(embed)
            
          await asyncio.sleep(mute_num*3600)
          for m in members:
            m.remove_roles(muted_role)
        if mute_for == 'mnt' or mute_for == 'minute' or mute_for == 'minutes' or mute_for == 'mnts':
          complete_time = str(mute_time)+mute_for
          await embed.add_field(name='Muted for: ', value=complete_time)
          if len(members) == 1:
            await ctx.send(embed2)
          else:
            await ctx.send(embed)
            
          await asyncio.sleep(mute_num*60)
          for m in members:
            m.remove_roles(muted_role)


        
        
        
        

        
      

       





    @commands.command(aliases=['L', 'Lock'])
    @commands.has_permissions(manage_messages=True)
    async def lock(self,ctx):
        guild = ctx.guild
        everyonerole = discord.utils.get(guild.roles, id=783547639944839178)   
        await ctx.channel.set_permissions(everyonerole, send_messages=False)
        embed = discord.Embed(title=f'{str(ctx.author.name)} locked {str(ctx.channel.name)}',
                              color=discord.Colour.dark_theme())
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['Unlock'])
    @commands.has_permissions(manage_messages=True)
    async def unlock(self,ctx):
        guild = ctx.guild
        everyonerole = discord.utils.get(guild.roles, id=783547639944839178)
        await ctx.channel.set_permissions(everyonerole, speak=True, send_messages=True)
        embed = discord.Embed(title=f'{str(ctx.author.name)} unlocked {str(ctx.channel.name)} 👍!',
                              color=discord.Colour.dark_theme())
        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx, member: discord.Member):
        guild = ctx.guild
        modrole = discord.utils.get(guild.roles, id=835924141419790356)
        logs = self.bot.get_channel(838363695036891147)
        mutedRole = discord.utils.get(guild.roles, id=783622936837226529)
        embedlog2 = discord.Embed(title=f'{member} has been unmuted.', color=discord.Colour.blue(),timestamp=datetime.datetime.utcnow())
        embedlog2.set_thumbnail(url=member.avatar_url)
        embed = discord.Embed(title=f" {member} has been unmuted!", color=discord.Colour.blue())
        if modrole not in member.roles:
            if mutedRole not in member.roles:
                await ctx.message.reply(f'> {member.name} was never muted!')
                return
            else:
                await member.remove_roles(mutedRole)
                await logs.send(embed=embedlog2)
                await ctx.send(embed=embed)
        else:
            await ctx.message.reply('> The mentioned member is a mod!')






async def setup(client):
    await client.add_cog(Mod(client))