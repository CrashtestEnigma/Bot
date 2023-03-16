import random
import os
from discord import Guild
import asyncio
import discord
import os
from discord.ext import commands

welcome_gifs = [
    'https://media.giphy.com/media/ehTzFBjQEyh8lQAn8b/giphy.gif',
    'https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif',
    'https://media.giphy.com/media/l4JyOCNEfXvVYEqB2/giphy.gif',
    'https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif',
    'https://media.giphy.com/media/kZzY6eKKPdIjK/giphy.gif',
    'https://media.giphy.com/media/H1TKAv5I5AOYcD7vxq/giphy.gif',
    'https://media.giphy.com/media/eIU6nUlmldCWl51FQH/giphy.gif',
]

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
	print("Bot is ready.")


@bot.event
async def on_member_join(member):

  print(f'{member} has joined the server.')
  channel = bot.get_channel(783547639944839182)
  strangers = bot.get_guild(783547639944839178)
  WelcCrew = strangers.get_role(894547700106797057)

  count = len(strangers.members)

  embed = discord.Embed(title='',
	                      description='',
	                      colour=discord.Colour.blue())
  embed.set_image(url=random.choice(welcome_gifs))
  embed.set_footer(text=f'You are our {count}th member!', icon_url=member.guild_avatar.url)

  if not member.bot:
    await channel.send(member.mention, embed=embed)

		

@bot.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):  # command to check ping
	embed = discord.Embed(colour=discord.Color.dark_theme())
	embed.set_image(
	    url=
	    "https://cdn.discordapp.com/attachments/810782980351983626/811180830654857237/typing.gif"
	)
	message = await ctx.send(embed=embed)
	await asyncio.sleep(1)
	embed.set_image(url='')
	embed.add_field(name="Ping:", value=f'{round(bot.latency * 1000)} ms')
	await message.edit(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def count(ctx):
	true_member_count = len([m for m in ctx.guild.members])
	embed = discord.Embed(color=discord.Colour.random())
	embed.add_field(name="Number of members:",
	                value=f'{true_member_count}')
	await ctx.send(embed=embed)


@bot.command()
@commands.has_role("Mod")
async def load(ctx, *, extension):
	try:
		bot.load_extension(f'cogs.{extension}')
		await ctx.send(f"Loaded `{extension}`")
	except discord.ext.commands.errors.ExtensionAlreadyLoaded:
		await ctx.send("Extension already loaded.")


@bot.command()
@commands.has_role("Mod")
async def unload(ctx, *, extension):
	bot.unload_extension(f'cogs.{extension}')
	await ctx.send(f"Unloaded `{extension}`")

@bot.event
async def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ["DISCORD_TOKEN"])
