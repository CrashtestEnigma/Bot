import discord
import os
import time
import asyncio
import re
import json
import aiohttp
from aiohttp import request
import praw
import time
import aiohttp
import discord.ext
import random_topic
import random
import datetime
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import youtube_dl
import time
import os
from gtts import gTTS
from discord.ext.commands import clean_content
from langcodes import Language
from rsap import RSAP
import requests


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Rexy is online boss.')
    @commands.command(name="rps", help = "rock , paper, scissors")
    async def rock_paper_scissors(self, context):
        choices = {
            0: "rock",
            1: "paper",
            2: "scissors"
        }
        reactions = {
            "🪨": 0,
            "🧻": 1,
            "✂": 2
        }
        embed = discord.Embed(title="Please choose", color= discord.Color.random())
        embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
        choose_message = await context.send(embed=embed)
        for emoji in reactions:
            await choose_message.add_reaction(emoji)

        def check(reaction, user):
            return user == context.message.author and str(reaction) in reactions

        try:
            reaction, user = await self.client.wait_for("reaction_add", timeout=10, check=check)

            user_choice_emote = reaction.emoji
            user_choice_index = reactions[user_choice_emote]

            bot_choice_emote = random.choice(list(reactions.keys()))
            bot_choice_index = reactions[bot_choice_emote]

            result_embed = discord.Embed(color= discord.Color.random())
            result_embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
            await choose_message.clear_reactions()

            if user_choice_index == bot_choice_index:
                result_embed.description = f"**That's a draw!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                
            elif user_choice_index == 0 and bot_choice_index == 2:
                result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
               
            elif user_choice_index == 1 and bot_choice_index == 0:
                result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                
            elif user_choice_index == 2 and bot_choice_index == 1:
                result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                
            else:
                result_embed.description = f"**I won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                

            await choose_message.edit(embed=result_embed)
        except asyncio.exceptions.TimeoutError:
            await choose_message.clear_reactions()
            timeout_embed = discord.Embed(title="Too late", color=discord.Color.random)
            timeout_embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
            await choose_message.edit(embed=timeout_embed)
    @commands.command(aliases = ["qu"], help = "generates a random conversation starter")
    async def question(self, ctx):
      topic=random_topic.get_topic()
      await ctx.send(topic)


    @commands.command()
    @commands.has_permissions(manage_emojis = True)
    async def say(self,ctx,*,text=None):
      if not text:
        await ctx.send("I need to know what to say pls")
        return
      vc = ctx.voice_client
      if not vc:
        await ctx.send("I need to be in a voice channel to do this, pls join one and use the join command")
        return
      tts =  gTTS(text = f"{text}", lang = "en")
      tts.save("text.mp3") 
      try:
        vc.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f"Finished playing {text}"))
        vc.source = discord.FFmpegPCMAudio(vc.source)
        vc.source.volume = 100
      except Exception:
        print("A problem occcured")  
    @commands.command(aliases = ["swl"])
    @commands.has_permissions(manage_emojis = True)
    async def say_with_language(self,ctx,n,*,text=None):
      if not text:
        await ctx.send("I need to know what to say pls")
        return
      vc = ctx.voice_client
      if not vc:
        await ctx.send("I need to be in a voice channel to do this, pls join one and use the join command")
        return
      m = Language.find(f"{n.lower()}")  
      tts =  gTTS(text = f"{text}", lang = f"{m}")
      tts.save("text.mp3") 
      try:
        vc.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f"Finished playing {text}"))
        vc.source = discord.FFmpegPCMAudio(vc.source)
        vc.source.volume = 100
      except Exception:
        print("A problem occcured")          


    @commands.command(aliases = ["c"]) 
    async def chat_(self, ctx,*,msg):
      headers = {"Authorization" : "BWlDbwTGnMGl"}
      url = "https://api.pgamerx.com/v5/ai"
      query = {"server": "main", "message" : f"{msg}","bot_name" : "The Stranger", "bot_master":"Ryuk, Hammy and Rexy","bot_gender": "Female", "bot_age" : "15" , "bot_location" : "The Internet", "bot_favorite_color" : "Black" }
      response = requests.request("GET", url, headers = headers, params = query)
      res = response.json()
      if "@everyone" in ctx.message.content.lower():
        return
      else:
        await ctx.send(res[0]["response"])

      


      


async def setup(client):
	await client.add_cog(fun(client)) 

