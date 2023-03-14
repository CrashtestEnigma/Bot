import discord
from discord.ext import commands


class Rules(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def rules(self, ctx):
      if ctx.channel == self.client.get_channel(803558384858300436):
        embed = discord.Embed(
            title="Rules.",
            description='By participating in this server, you agree to abide by these rules. You can ask one of the mods if you need clarification!',
            colour=discord.Colour.green()

        )
        embed.add_field(name="Rule 1", value="Follow the [Discord Community Guidelines]("
                                             "https://discord.com/guidelines) and [Terms of Service]("
                                             "https://discord.com/terms).", inline=False)
        embed.add_field(name="Rule 2", value='Follow the [Strangers Code of Conduct]('
                                             'https://shinigami07991.medium.com/rules-8ee8b6039248).', inline=False)
        embed.add_field(name='Rule 3', value='Listen to and respect staff members, and their decisions.', inline=False)
        embed.add_field(name='Rule 4', value='Please speak English to the best of your ability, as this is an English '
                                             'speaking server (Except for channels meant for this).', inline=False)
        embed.add_field(name='Rule 5', value="We don't allow advertisements or promotions, so please refrain from "
                                             "doing those.", inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=["Rule1"])
    @commands.has_permissions(manage_messages=True)
    async def rule1(self, ctx,  *members: discord.Member):
        if members is None:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name="Rule 1", value="Follow the [Discord Community Guidelines]("
                                                 "https://discord.com/guidelines) and [Terms of Service]("
                                                 "https://discord.com/terms).", inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name="Rule 1", value="Follow the [Discord Community Guidelines]("
                                                 "https://discord.com/guidelines) and [Terms of Service]("
                                                 "https://discord.com/terms).", inline=False)
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command(aliases=["Rule2"])
    @commands.has_permissions(manage_messages=True)
    async def rule2(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name="Rule 2", value='Follow the [Strangers Code of Conduct]('
                                                 'https://shinigami07991.medium.com/rules-8ee8b6039248).', inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name="Rule 2", value='Follow the [Strangers Code of Conduct]('
                                                 'https://shinigami07991.medium.com/rules-8ee8b6039248).', inline=False)
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command(aliases=["Rule3"])
    @commands.has_permissions(manage_messages=True)
    async def rule3(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name='Rule 3', value='Listen to and respect staff members, and their decisions.',
                            inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name='Rule 3', value='Listen to and respect staff members, and their decisions.',
                            inline=False)
            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command(aliases=["Rule4"])
    @commands.has_permissions(manage_messages=True)
    async def rule4(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name='Rule 4', value="Please speak English to the best of your ability, as this is an English speaking server(Except for channels meant for this).", inline=False)

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name='Rule 4', value="Please speak English to the best of your ability, as this is an English speaking server (Except for channels meant for this).", inline=False)

            await ctx.send(" ".join([member.mention for member in members]), embed=embed)

    @commands.command(aliases=["Rule5"])
    @commands.has_permissions(manage_messages=True)
    async def rule5(self, ctx, *members: discord.Member):
        if members is None:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name='Rule 5', value="We don't allow advertisements or promotions, so please refrain from doing those.", inline=False)

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=discord.Colour.green())
            embed.add_field(name='Rule 4', value="We don't allow advertisements or promotions, so please refrain from "
                                                 "doing those.", inline=False)

            await ctx.send(" ".join([member.mention for member in members]), embed=embed)


async def setup(client):
    await client.add_cog(Rules(client))
