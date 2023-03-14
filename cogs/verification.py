import discord
from discord.ext import commands
from googleapiclient.discovery import build
import datetime


class Verification(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
      strangers = self.client.get_guild(783547639944839178)
      await strangers.fetch_roles()
      verify_channel = self.client.get_channel(883318979039465523)

      if message.channel.id == verify_channel.id:
        if message.attachments:
          await message.add_reaction('<:checkemoji:885481014091214878>')
          await message.add_reaction('<:crossemoji:885481014162497536>')

          await message.channel.send('Please wait for a mod to verify you.', delete_after=10)

          #########################################################

  
          modrole = discord.utils.get(strangers.roles, name='Mod')
          mods = []
          for member in strangers.members:
            if modrole in member.roles:
              if not member.bot:
                mods.append(member)
              
          def check1(reaction, user):
              return user in mods and str(reaction.emoji) == '<:checkemoji:885481014091214878>'
          def check2(reaction, user):
              return user in mods and str(reaction.emoji) == '<:crossemoji:885481014162497536>'

          print('checks here')
          verifiedrole= strangers.get_role(822424845144031263)
          print(f'this is the verified role: {verifiedrole}')
          print(f"this is verifiedrole's type: {type(verifiedrole)}")

          await strangers.fetch_roles()

          try:
            reaction, user = await self.client.wait_for('reaction_add', check=check1)
            print('at line 47')
            await message.author.add_roles(verifiedrole)
            await message.author.send('You have been verified in The Strangers!')
            print('reacted with check')
          except Exception as e:
            print(e)
            print('smth went wrong: checkmark')
          ###############################################################
          try:
            reaction, user = await self.client.wait_for('reaction_add', check=check2)
            await message.author.send('Your verification request in The Strangers was denied. Contact the moderators if you think this action was taken by accident.')
            print('reacted with cross')
          except Exception:
            print('smth went wrong: cross')
              



async def setup(client):
    await client.add_cog(Verification(client))