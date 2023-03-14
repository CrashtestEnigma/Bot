import datetime
import discord
from discord.ext import commands
import asyncio
import contextlib
import re
import random


class WhoSaidThis(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def collecteveryone(self, ctx):
        ryuk = discord.utils.get(ctx.message.guild.members, name='Ryuk.')
        if ctx.author == ryuk:

            await ctx.channel.send('Initiating message hunt...')

            general = ctx.message.guild.get_channel(783547639944839182)
            myserver = self.client.get_guild(692986387120783411)

            ryuk_channel = discord.utils.get(myserver.text_channels, name='ryuk')
            rexy_channel = discord.utils.get(myserver.text_channels, name='rexy')
            zakk_channel = discord.utils.get(myserver.text_channels, name='zakk')
            hammy_channel = discord.utils.get(myserver.text_channels, name='hammy')
            everyone_channel = discord.utils.get(myserver.text_channels, name='everyone')

            twelveam = datetime.datetime(2021, 6, 9, 18, 30)
            oneam = datetime.datetime(2021, 6, 9, 19, 30)
            fourpm = datetime.datetime(2021, 6, 6, 11, 26)
            fivepm = datetime.datetime(2021, 6, 6, 12, 00)

            messages = await general.history(limit=None, before=oneam, after=twelveam, oldest_first=True).flatten()

            altmessages = await general.history(limit=None, before=fivepm, after=fourpm, oldest_first=True).flatten()

            print('NUMBER OF MESSAGES: ' + str(len(messages)))
            print('NUMBER OF ALT MESSAGES: ' + str(len(altmessages)))

            rexy = discord.utils.get(ctx.message.guild.members, name='Mansib')
            zakk = discord.utils.get(ctx.message.guild.members, name='Zakk')
            hammy = discord.utils.get(ctx.message.guild.members, name='HAMMY')
            hammy2 = discord.utils.get(ctx.message.guild.members, name='Hammy 2.0')

            rexys_messages = []
            ryuks_messages = []
            zakks_messages = []
            hammys_messages = []
            hammy2s_messages = []

            for message in messages:
                if message.author == rexy:
                    if len(message.content) >= 20:
                        rexys_messages.append(message)
                elif message.author == ryuk:
                    if len(message.content) >= 20:
                        ryuks_messages.append(message)
                elif message.author == zakk:
                    if len(message.content) >= 20:
                        zakks_messages.append(message)
                elif message.author == hammy:
                    if len(message.content) >= 20:
                        hammys_messages.append(message)

            for m in altmessages:
                if m.author == hammy2:
                    if len(m.content) >= 20:
                        hammys_messages.append(m)

            test_channel = discord.utils.get(self.client.get_all_channels(), guild__name='Lonesomenesss', name='test')

            number_of_rexy = len(rexys_messages)
            number_of_ryuk = len(ryuks_messages)
            number_of_zakk = len(zakks_messages)
            number_of_hammy = len(hammys_messages)
            number_of_hammy2 = len(hammy2s_messages)

            print('REXY: ' + str(number_of_rexy))
            print('RYUK: ' + str(number_of_ryuk))
            print('ZAKK: ' + str(number_of_zakk))
            print('HAMMY: ' + str(number_of_hammy))
            print('HAMMY 2.0: ' + str(number_of_hammy2))

            everyones_messages = rexys_messages + ryuks_messages + zakks_messages + hammy2s_messages

            for m in everyones_messages:
                everyone_channel.send(m)

            await ctx.channel.send('OK DONE THAT TOOK A WHILE BUT I DID IT') 

    @commands.command()
    async def whosaidthis(self, ctx):

        global everyones_messages_in_channel, eM2, rY2, rE2, zA2, hA2

        myserver = self.client.get_guild(692986387120783411)
        ryuk_channel = discord.utils.get(myserver.text_channels, name='ryuk')
        rexy_channel = discord.utils.get(myserver.text_channels, name='rexy')
        zakk_channel = discord.utils.get(myserver.text_channels, name='zakk')
        hammy_channel = discord.utils.get(myserver.text_channels, name='hammy')
        everyone_channel = discord.utils.get(myserver.text_channels, name='everyone')

        whosaidthis_embed1 = discord.Embed(
            title=' ❓ Who said this ❓',
            description='Guess who said these sentences from the server. React to participate.',
            color=discord.Color.red()
        )
        whosaidthis_embed1.set_footer(text='Still in beta, so there are sentences from only four members.',
                                      icon_url=ctx.author.avatar_url)

        theembeditself = await ctx.send(embed=whosaidthis_embed1)
        await theembeditself.add_reaction('👀')
        users = []
        user_names = []
        user_ids = []

        for y in users:
            user_ids.append(y.id)

        def check(r, u):
            if r.message == theembeditself and str(r.emoji) == '👀':
                if not u.bot:
                    users.append(u)

        try:
            await self.client.wait_for('reaction_add', check=check, timeout=5)

        except asyncio.TimeoutError:
            for x in users:
                user_names.append(x.name)

            if len(users) == 0:
                await ctx.send('No one wants to play? Fine.')
                return
            else:
                await ctx.send(f"Participants: `{user_names}`. Commence the game!")

            await ctx.channel.fetch_message(id=theembeditself.id)

            ryuks_messages_in_channel = await ryuk_channel.history(limit=None).flatten()
            rexys_messages_in_channel = await rexy_channel.history(limit=None).flatten()
            zakks_messages_in_channel = await zakk_channel.history(limit=None).flatten()
            hammys_messages_in_channel = await hammy_channel.history(limit=None).flatten()
            everyones_messages_in_channel = await everyone_channel.history(limit=None).flatten()

            eM2 = []
            rY2 = []
            rE2 = []
            zA2 = []
            hA2 = []

            for m in everyones_messages_in_channel:
                eM2.append(m.content)
            for m in ryuks_messages_in_channel:
                rY2.append(m.content)
            for m in rexys_messages_in_channel:
                rE2.append(m.content)
            for m in zakks_messages_in_channel:
                zA2.append(m.content)
            for m in hammys_messages_in_channel:
                hA2.append(m.content)

        question_embed = discord.Embed(
            title='Who said this?',
            description=str(random.choice(eM2)),
            color=discord.Color.green()
        )
        await ctx.send(embed=question_embed)

        for x in range(3):

            while True:

                try:
                    msg = await self.client.wait_for(
                        "message",
                        timeout=10,
                        check=lambda message: message.author in users
                                              and message.channel == ctx.channel)

                    if msg.content.lower() == 'ryuk' and question_embed.description in rY2:
                        await msg.add_reaction('✅')
                    elif msg.content.lower() == 'rexy' and question_embed.description in rE2:
                        await msg.add_reaction('✅')
                    elif msg.content.lower() == 'zakk' and question_embed.description in zA2:
                        await msg.add_reaction('✅')
                    elif msg.content.lower() == 'hammy' and question_embed.description in hA2:
                        await msg.add_reaction('✅')
                    else:
                        pass

                except asyncio.TimeoutError:
                    await ctx.channel.send('Coming up...')


async def setup(client):
    await client.add_cog(WhoSaidThis(client))
