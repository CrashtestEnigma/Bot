import discord
from discord.ext import commands
import asyncio


class Snippets(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rich(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.purple()
            )
            embed.set_image(url='https://cdn.discordapp.com/attachments/692986387120783415/807173510924992512/rich1.jpg')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.purple()
            )
            embed.set_image(url='https://cdn.discordapp.com/attachments/692986387120783415/807173510924992512/rich1.jpg')
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command()
    async def bang(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.purple()
            )
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/783547639944839182/807526283302404146/2021-02-06_2.png')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.purple()
            )
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/783547639944839182/807526283302404146/2021-02-06_2.png')
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command()
    async def sfw(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='Please keep the chat appropriate and SFW.',
                colour=discord.Colour.blue()
            )
            embed.set_footer(text='')
            embed.set_author(name='Mod says:',
                             icon_url='https://cdn.discordapp.com/avatars/612928662953656320/12ff06f277d2bb5c3fa4828e24c0d7f9.png?size=128')
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title='',
                description='Please keep the chat appropriate and SFW.',
                colour=discord.Colour.blue()
            )
            embed.set_footer(text='')
            embed.set_author(name='Mod says:',
                             icon_url='https://cdn.discordapp.com/avatars/612928662953656320/12ff06f277d2bb5c3fa4828e24c0d7f9.png?size=128')
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)


    @commands.command()
    async def liar(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.magenta()
            )
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/783547639944839182/812589891246096424/2021-02-20_2.png ')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='',
                description='',
                colour=discord.Colour.purple()
            )
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/783547639944839182/812589891246096424/2021-02-20_2.png ')
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command(aliases=['whyeng'])
    async def whyenglish(self, ctx):
      embed=discord.Embed(
        title='Why English is important here.',
        description='Please know that speaking English is important to ensure no one feels left out in chat, it is a language understood by everyone in this server. Speaking other languages may lead to some people feeling left out, which is the total opposite of what we want to achieve :)',
        color=discord.Color.green()
      )
      await ctx.send(embed=embed)
      


async def setup(client):
    await client.add_cog(Snippets(client))
