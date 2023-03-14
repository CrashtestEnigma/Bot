import discord
from discord.ext import commands
from googleapiclient.discovery import build
import datetime


class TestIt(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['evaltext', 'Evaltext', 'eval'])
    async def evaluatetext(self, ctx, *, query):
        API_KEY = 'AIzaSyATerMFpQ3vgDRxzjpOseLsJThM2AdSgd8'

        client = build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=API_KEY,
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            
        )

        #########################################################################################################################
        severe_toxicity = {
            'comment': {'text': query},
            'requestedAttributes': {'SEVERE_TOXICITY': {}}
        }

        severe_toxicity_response = client.comments().analyze(body=severe_toxicity).execute()
        STscore = severe_toxicity_response['attributeScores']['SEVERE_TOXICITY']['spanScores'][0]['score']['value']

        #########################################################################################################################

        identity_attack = {
            'comment': {'text': query},
            'requestedAttributes': {'IDENTITY_ATTACK': {}}
        }

        identity_attack_response = client.comments().analyze(body=identity_attack).execute()
        IAscore = identity_attack_response['attributeScores']['IDENTITY_ATTACK']['spanScores'][0]['score']['value']

        #########################################################################################################################

        threat = {
            'comment': {'text': query},
            'requestedAttributes': {'THREAT': {}}
        }

        threat_response = client.comments().analyze(body=threat).execute()
        THREATscore = threat_response['attributeScores']['THREAT']['spanScores'][0]['score']['value']
        #########################################################################################################################

        explicit = {
            'comment': {'text': query},
            'requestedAttributes': {'SEXUALLY_EXPLICIT': {}}
        }

        explicit_response = client.comments().analyze(body=explicit).execute()
        EXPLICITscore = explicit_response['attributeScores']['SEXUALLY_EXPLICIT']['spanScores'][0]['score']['value']

        #########################################################################################################################
        insult = {
            'comment': {'text': query},
            'requestedAttributes': {'INSULT': {}}
        }

        insult_response = client.comments().analyze(body=insult).execute()
        INSULTscore = explicit_response['attributeScores']['INSULT']['spanScores'][0]['score']['value']

        ##########################################################################################################################


        embed = discord.Embed(
            title='Text Evaluation',
            description=query,
            color=discord.Color.green()
        )
        embed.add_field(name='SEVERE_TOXICITY: ', value=round(STscore, 3), inline=True)
        embed.add_field(name='IDENTITY_ATTACK: ', value=round(IAscore, 3), inline=True)
        embed.add_field(name='THREAT: ', value=round(THREATscore, 3), inline=True)
        embed.add_field(name='SEXUALLY_EXPLICIT: ', value=round(EXPLICITscore, 3), inline=True)
        embed.add_field(name='INSULT:', value=round(INSULTscore, 3), inline=True)

        await ctx.send(embed=embed)



async def setup(client):
    await client.add_cog(TestIt(client))
