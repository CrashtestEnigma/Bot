import discord
from discord.ext import commands
import asyncio


class Echo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
          
            title='What do you want to repeat?',
            description='||This request will timeout after 1 minute.||'
        )
        sent = await ctx.send(embed=embed)

        try:
            msg = await self.client.wait_for(
                "message",
                timeout=60,
                check=lambda message: message.author == ctx.author
                                      and message.channel == ctx.channel
            )
            if msg:
                await sent.delete()
                await msg.delete()
                await ctx.send(msg.content)

        except asyncio.TimeoutError:
            await sent.delete()
            await ctx.send('Cancelling due to timeout...', delete_after=10)


async def setup(client):
    await client.add_cog(Echo(client))

