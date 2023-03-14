import discord
from discord.ext import commands
import asyncio
import re
import sqlite3
import random
from datetime import datetime, date, timedelta


class Interactivity(commands.Cog):
    def __init__(self, client):
        self.client = client
#
#    @commands.Cog.listener()
  #  async def on_message(self, message):
      #  db = sqlite3.connect('INTERACTIVITY.db')
     #   c = db.cursor()
       # c.execute(f"CREATE TABLE messages(id INTEGER PRIMARY KEY, msg TEXT, author INTEGER)")
      #  print('Table created successfully.')

        #c.execute(
        #    f"INSERT INTO messages(msg, author) VALUES({message}, #{message.author.id})"
     #   )

     #   db.commit()
     #   print("Records created successfully")
      #  db.close()

      #  lowercasemsg = message.lower()

      #  for member in message.guild.members:
      #      if member.mentioned_in(message) and 'welcome' in lowercasemsg:
         #       if date(member.joined_at) - date(datetime.datetime.now()) #< timedelta(days=1):

          #              c.execute(f"SELECT FROM info WHERE msg=  author=#{message.author.id}")
                #        result = c.fetchone()

                        
                          

                    

async def setup(client):
    await client.add_cog(Interactivity(client))
