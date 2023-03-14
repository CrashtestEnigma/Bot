from discord.ext import commands
import discord
from googletrans import Translator
from langcodes import Language
from langdetect import DetectorFactory, detect

DetectorFactory.seed = 0
translator = Translator()


class Translation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["tl", "Tl", "Translate", "TL"])
    async def translate(self, ctx, *, message):
        global language
        language = translator.detect(message)
        translation = translator.translate(message)
        embed = discord.Embed(color=discord.Color.dark_theme())
        intelligible_language = Language.get(f'{language.lang}').display_name()
        embed.add_field(name=f"Language: {intelligible_language} ", value=f'{translation.text}')
        embed.set_footer(text='Powered by Google Translate', icon_url='https://media.discordapp.net/attachments'
                                                                      '/692986387120783415/833998282770087976'
                                                                      '/google_translate.png?width=670&height=670')
        await ctx.send(embed=embed)    
      

async def setup(client):
    await client.add_cog(Translation(client))
