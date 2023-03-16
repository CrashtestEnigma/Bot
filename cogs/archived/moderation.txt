import discord
from discord.ext import commands
import googleapiclient
from googleapiclient.discovery import build
import datetime


class AutoMod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):

        if msg.content:

            API_KEY = 'AIzaSyATerMFpQ3vgDRxzjpOseLsJThM2AdSgd8'

            client = build(
                "commentanalyzer",
                "v1alpha1",
                developerKey=API_KEY,
                discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            )
            #########################################################################################################################
            severe_toxicity = {
                'comment': {'text': msg.content},
                "languages": ["en"],
                'requestedAttributes': {'SEVERE_TOXICITY': {}}
            }
          
            severe_toxicity_response = client.comments().analyze(body=severe_toxicity).execute()
            STscore = severe_toxicity_response['attributeScores']['SEVERE_TOXICITY']['summaryScore']['value']

            #########################################################################################################################

            identity_attack = {
                'comment': {'text': msg.content},
                "languages": ["en"],
                'requestedAttributes': {'IDENTITY_ATTACK': {}}
            }

            identity_attack_response = client.comments().analyze(body=identity_attack).execute()
            IAscore = identity_attack_response['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value']

            #########################################################################################################################

            threat = {
                'comment': {'text': msg.content},
                "languages": ["en"],
                'requestedAttributes': {'THREAT': {}}
            }

            threat_response = client.comments().analyze(body=threat).execute()
            THREATscore = threat_response['attributeScores']['THREAT']['summaryScore']['value']
            #########################################################################################################################

            
            explicit = {
                'comment': {'text': msg.content},
                "languages": ["en"],
                'requestedAttributes': {'SEXUALLY_EXPLICIT': {}}
            }

            explicit_response = client.comments().analyze(body=explicit).execute()
            EXPLICITscore = explicit_response['attributeScores']['SEXUALLY_EXPLICIT']['summaryScore']['value']
            #########################################################################################################################    
            insult = {
                'comment': {'text': msg.content},
                "languages": ["en"],
                'requestedAttributes': {'INSULT': {}}
            }

            insult_response = client.comments().analyze(body=insult).execute()
            INSULTscore = explicit_response['attributeScores']['INSULT']['summaryScore']['value']
            
            mod_role= discord.utils.get(msg.guild.roles, name='Mod')
            strangers = self.client.get_guild(id=783547639944839178)
            ryuk = strangers.get_member(user_id=612928662953656320)
            serious_channel = self.client.get_channel(884699085234405376)

          
            if msg:
                if STscore >= 0.75:
                        await msg.delete()
                if IAscore >= 0.8:
                        await msg.delete()
                if THREATscore >= 0.75:
                        await msg.delete()
                if EXPLICITscore >= 0.75:
                        await msg.delete()
                if INSULTscore >= 0.75:
                        await msg.delete()
                
                          

              
          
async def setup(client):
    await client.add_cog(AutoMod(client))
