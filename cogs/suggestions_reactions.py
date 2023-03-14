import discord
from discord.ext import commands

class Suggestions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        strangers = self.client.get_guild(783547639944839178)
        if msg.guild == strangers:
            staff = discord.utils.get(msg.guild.roles, name='Staff')
            sentence = msg.content.split(" ")
            if not msg.author.bot:
              if staff not in msg.author.roles:
                  if msg.channel.id == 821343742128291850:
                      if sentence[0] == "Suggestion:":
                          await msg.add_reaction("✅")
                          await msg.add_reaction("❌")

                      else:
                          await msg.delete()
                          await msg.channel.send('Please use `Suggestion:` at the start of your message.', delete_after=5)
                        

            else:
                pass


async def setup(client):
    await client.add_cog(Suggestions(client))