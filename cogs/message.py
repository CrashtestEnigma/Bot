import discord
from discord.ext import commands
import asyncio


class Message(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.lower == 'welcome':
            strangers = discord.utils.get(self.client.guilds,
                                          name='The Strangers')
            botrole = discord.utils.get(strangers.roles, name='Bots')

            for m in strangers.members:
                if m.bot:
                    await m.add_roles(botrole)
                    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def bot(self, ctx, member:discord.Member):
      if member.bot:
        await ctx.send(f'{member} is a bot.')
      else:
        await ctx.send(f'{member} is not a bot.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def grand(self, ctx):    
      embed= discord.Embed(
        title='Booster Perks',
        description="Since the server now has 13 boosts, we are 1 boost away from lvl 3. To celebrate when the server achieves lvl 3, here are the perks for the first person who boosts it to lvl 3 by 1 boost.",
        color=discord.Color.magenta()
      )

      embed.add_field(name='Perk 1' , value = "2 extra custom roles for a total of 3 custom roles.")
      embed.add_field(name='Perk 2' , value = "Custom channel named after you, for 30 days.")
      
      #can we add new line in the same field? with different names? bruv u do it. ok lemme try #3 ig? #hows it looking
    #cool
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/899595264082468864/928290843293532201/9390-nitrogem.gif')
      embed.set_footer(text='Boost now!', icon_url='https://cdn.discordapp.com/attachments/899595264082468864/928299082156482570/1907-nitro-boosting-level.gif')

      await ctx.send('@everyone', embed=embed)
#the run and stop button... its stuck on "stopping" #oh ok
#
    @commands.command()
    async def wishclaw(self, ctx):
      general = self.client.get_channel(783547639944839182)
      await general.send(f" @here It's the birthday of one of our most iconic members, CLAWDEEN!!! Wish her a sweet 16!")
      await ctx.send("Bhej diya.")

async def setup(client):
    await client.add_cog(Message(client))
