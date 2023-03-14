import discord
from discord.ext import commands


class Search(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def search(self, ctx, member: discord.Member, *, keywords):
        counter = 0
        search_result = []
        member_history = []
        search_channel = ctx.channel
        messages = await search_channel.history(limit=10000000000000000000, oldest_first=True).flatten()
        for message in messages:
            if message.author == member:
                member_history.append(message)
            else:
                pass
        for each_message in member_history:
            if keywords.lower() in each_message.content.lower():
                counter = counter + 1
                search_result.append(each_message)
            else:
                pass

        embed = discord.Embed(
            title=f'How many times has {member.display_name} said {keywords}?',
            description=str(counter),
            color=discord.Color.dark_red()
        )
        await ctx.send(embed=embed)



async def setup(client):
    await client.add_cog(Search(client))
