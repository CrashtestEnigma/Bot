import discord
from discord.ext import commands
import random
import asyncio
import time
import sqlite3
from PyDictionary import PyDictionary

hug_gifs = ['https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif',
            'https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif',
            'https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif',
            'https://media.giphy.com/media/3bdGMdcWTIto24a8vK/giphy.gif',
            'https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif',
            'https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif',
            'https://media.giphy.com/media/2GnS81AihShS8/giphy.gif',
            ]

welcome_gifs = ['https://media.giphy.com/media/ehTzFBjQEyh8lQAn8b/giphy.gif',
                'https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif',
                'https://media.giphy.com/media/l4JyOCNEfXvVYEqB2/giphy.gif',
                'https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif',
                ]


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    # 8ball command
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Dont count on it.',
                     'It is certain.',
                     'It is decidedly so.', ]

        await ctx.send(f'{random.choice(responses)}')

    # spam warning embed
    @commands.command()
    async def spam(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='Please do not spam the chat.',
                colour=discord.Colour.blue()
            )
            embed.set_footer(text='')
            embed.set_author(name='Mod says:',
                             icon_url='https://cdn.discordapp.com/avatars/745674627845587004/834f65d2747b1bb8806d12e3791c36bd.webp?size=1024')
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title='',
                description='Please do not spam the chat.',
                colour=discord.Colour.blue()
            )
            embed.set_footer(text='')
            embed.set_author(name='Mod says:',
                             icon_url='https://cdn.discordapp.com/avatars/745674627845587004/834f65d2747b1bb8806d12e3791c36bd.webp?size=1024')
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    # hug gif
    @commands.command(aliases=['huggie wuggie', 'huggie'])
    async def hug(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url=random.choice(hug_gifs))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url=random.choice(hug_gifs))
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    # welcome gif
    @commands.command()
    async def welcome(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url=random.choice(welcome_gifs))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url=random.choice(welcome_gifs))
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command()
    async def breathtaking(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url='https://media.giphy.com/media/hv4TC2Ide8rDoXy0iK/giphy.gif')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url='https://media.giphy.com/media/hv4TC2Ide8rDoXy0iK/giphy.gif')
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command()
    async def cya(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.purple()
            )
            embed.set_image(url='https://media.giphy.com/media/Ru9sjtZ09XOEg/giphy.gif')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.purple()
            )
            embed.set_image(url='https://media.giphy.com/media/Ru9sjtZ09XOEg/giphy.gif')
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command()
    async def hugz(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url='https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif')
            message = await ctx.send(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/3bdGMdcWTIto24a8vK/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/2GnS81AihShS8/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)


        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.blue()
            )
            embed.set_image(url='https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif')
            message = await ctx.send(" ".join([member.mention for member in members]), embed=embed)
            embed.set_image(url='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/3bdGMdcWTIto24a8vK/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)
            embed.set_image(url='https://media.giphy.com/media/2GnS81AihShS8/giphy.gif')
            await asyncio.sleep(1)
            await message.edit(embed=embed)

    @commands.command()
    async def skribbl(self, ctx):
        embed=discord.Embed(
            title='SKRIBBLE EVENTS',
            description='React if you want to get notified.',
            colour=discord.Color.dark_grey()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/692986387120783415/840581561954467850'
                            '/skribble_events.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def transpose(self, ctx, *, name):
        NAME = name
        ryuk = discord.utils.get(ctx.guild.members, name='Ryuk.')
        if ctx.author == ryuk:
            for member in ctx.guild.members:
                if member == ryuk:
                    continue

                try:
                  await member.edit(nick=NAME)
                except discord.DiscordException:
                  continue

    @commands.command()
    async def change(self, ctx, *, name):
        NAME = name
        ryuk = discord.utils.get(ctx.guild.members, name='Ryuk.')
        if ctx.author == ryuk:
          for x in range(10):
            for member in ctx.guild.members:
                if member == ryuk:
                    continue
                await member.edit(nick=NAME)  
    
    @commands.command()
    async def howmany(self, ctx, *, name):
      count = 0
      for m in ctx.guild.members:
        if m.nick == name:
          count = count + 1
      await ctx.send(f'There are `{count}` members named {name} in the server.')
    


    @commands.command()
    async def stripaway(self, ctx):
        ryuk = discord.utils.get(ctx.guild.members, name='Ryuk.')
        if ctx.author == ryuk:
            for member in ctx.guild.members:
                if member == ryuk:
                    continue
                await member.edit(nick=None)

    @commands.command()
    async def stripawaybots(self, ctx):
        await ctx.send("Clearing all bots' nicknames...")
        ryuk = discord.utils.get(ctx.guild.members, name='Ryuk.')
        if ctx.author == ryuk:
            for member in ctx.guild.members:
              if member.bot:
                await member.edit(nick=None)

    @commands.command()
    async def on_message(self, message):
      if message.content.startswith(':'):
         if 'vampy' in message.content:
          await message.delete() 
      else:
        print('nope')

    @commands.command()
    async def spamdm(self, ctx, member: discord.Member, amount=1, *, content=None):
        if ctx.author.name == 'Ryuk.':
            for i in range(amount):
                channel = await member.create_dm()
                await channel.send(content)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def betterpoll(self, ctx, *, options):
      options_list = options.split(',')
      emoji_list = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
      embed=discord.Embed(
        color=discord.Color.green()
      )
      for i in range(len(options_list)):
        embed.add_field(name=emoji_list[i], value=options_list[i], inline=False)

      msg = await ctx.send(embed=embed)

      for i in range(len(options_list)):
        await msg.add_reaction(emoji_list[i])

    @commands.command(aliases=['m','M'])
    async def meaning(ctx,word):
      dictionary=PyDictionary()
      meaning=dictionary.meaning(word)
      embed=discord.Embed(title=f'{word} means-',description=meaning, color=discord.Colour.blue())
      await ctx.channel.send(embed=embed)

    @commands.command(aliases=['hbd', 'Hbd'])
    async def happybirthday(self, ctx, member:discord.Member):
      strangers = self.client.get_guild(783547639944839178)
      hbdrole = discord.utils.get(strangers.roles, id=832855834798063657)
      
      await member.add_roles(hbdrole)
      await ctx.send('Added the happy birthday role.')
  
    @commands.command()
    async def ruleembed(self, ctx, kind, number:int, *, content=None):
      strangers = self.client.get_guild(783547639944839178)
      ruleschannel = discord.utils.get(strangers.text_channels, id=803558384858300436)
      rules_message = await ruleschannel.fetch_message(809038460308422677)
      rules_embed= rules_message.embeds[0]

      field = rules_embed.fields[number-1]
      print(field.value)

      for f in rules_embed.fields:
        print(f.name)

      if kind == 'edit' or kind == 'e':
        nameoffield = rules_embed.fields[number-1].name
        rules_embed.set_field_at(number, name=nameoffield, value=content)
        await rules_message.edit(embed=rules_embed)
        await ctx.send(f'Edited rule no. {number}')

      if kind == 'delete' or kind == 'd':
        rules_embed.remove_field(number-1)
        await rules_message.edit(embed=rules_embed)
        await ctx.send(f'Deleted rule no. {number}')

    @commands.command()
    async def string(self, ctx, *, message):
      await ctx.send(str(message))

    @commands.command(aliases=['rc'])
    @commands.has_permissions(manage_messages=True)
    async def rolecount(self, ctx, *, role:discord.Role):
      c=0
      try:
        roletofind=discord.utils.get(ctx.guild.roles,name=role.name)
        for member in ctx.guild.members:
          if roletofind in member.roles:
            c=c+1
        embed=discord.Embed(
          title=roletofind.name,
          description= f'Holders: {c}',
          color=discord.Color.red()
        )

        await ctx.send(embed=embed)
      except discord.ext.commands.errors.RoleNotFound:
        await ctx.send(f'No role named `{role}` found.')

      
    @commands.command()
    async def wishrexy(self, ctx):
      embed=discord.Embed(title='Message from Ryuk:', description="A very happy birthday to Momo and Rexy, please make sure to wish them!", color=discord.Color.green())
      embed.set_footer(text="Sorry for not being here guys.")
                          
      general=self.client.get_channel(id=783547639944839182)
      await general.send(f"<@647796364205359123> <@731385001131769877>",embed=embed)


   
    

async def setup(client):
    await client.add_cog(Misc(client))
