import discord
import sqlite3
from discord.ext import commands
from time import sleep

intents = discord.Intents.all()
intents.members = True


class intro(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=['Intro'])
    @commands.cooldown(1, 90, commands.BucketType.user)
    async def intro(self, ctx):
        guild = ctx.guild
        make_intro = self.bot.get_channel(784758643722551326)
        intro = self.bot.get_channel(826417651466108959)
        if ctx.channel == make_intro:
            embed = discord.Embed(description='What is your name? ',
                                  color=discord.Colour.dark_theme())
            embed_2 = discord.Embed(description=' How old are you?',
                                    color=discord.Colour.dark_theme())

            embed_3 = discord.Embed(description='Where do you live? ',
                                    color=discord.Colour.dark_theme())
            embed_4 = discord.Embed(
                description='What are your hobbies or interests? ',
                color=discord.Colour.dark_theme())
            embed_6 = discord.Embed(
                description=
                'What is your gender?  ```Male , Female , Non-binary or Others```',
                color=discord.Colour.dark_theme())
            await make_intro.send(embed=embed)
            test = False

            def check(m):
                return m.channel == make_intro and m.author == ctx.author

            x = True
            while x:
                name = await self.bot.wait_for('message', check=check)
                if name.content.isdigit():
                    await make_intro.send(
                        '```Your answer should not include numbers!```')
                    continue
                elif name.content == '+END':
                    return
                else:
                    await make_intro.send(embed=embed_2)
                    x = False

                    def check2(m2):
                        return m2.channel == make_intro and m2.author == ctx.author

                    x1 = True
                    while x1:
                        age = await self.bot.wait_for('message', check=check2)
                        if age.content.isdigit():
                            if int(age.content) <= 12:
                                await ctx.channel.send(
                                    '```You know you cannot use discord if you are 12 or below? Enter your real age -_- ```'
                                )
                                continue
                            elif int(age.content) >= 60:
                                await ctx.channel.send(
                                    '```Pretty old eh? Mind entering your real age again?```'
                                )
                                continue
                            else:
                                await ctx.send(embed=embed_6)
                                x1 = False
                        elif age.content == '+END':
                            return
                        else:
                            await make_intro.send(
                                '```Your age connot be a word! Make sure there are no alphabets in your answer!``` '
                            )
                            continue

                        def check3(m3):
                            return m3.channel == make_intro and m3.author == ctx.author

                        x2 = True
                        while x2:
                            gender = await self.bot.wait_for('message',
                                                             check=check3)
                            if 'male' == gender.content.lower(
                            ) or 'female' == gender.content.lower(
                            ) or 'non-binary' == gender.content.lower(
                            ) or 'Male' == gender.content.lower(
                            ) or 'Female' == gender.content.lower(
                            ) or 'Non-binary' == gender.content.lower(
                            ) or 'others' == gender.content.lower(
                            ) or 'Others' == gender.content.lower():
                                await make_intro.send(embed=embed_3)
                                x2 = False
                            elif gender.content == '+END':
                                return
                            else:
                                await make_intro.send(
                                    '```That is not a valid answer!``` ')
                                continue

                            def check4(m4):
                                return m4.channel == make_intro and m4.author == ctx.author

                            x3 = True
                            while x3:
                                location = await self.bot.wait_for(
                                    'message', check=check4)
                                if location.content.isdigit():
                                    await make_intro.send(
                                        '```You do not live in a number, do you? -_-```'
                                    )
                                    continue
                                elif location.content == '+END':
                                    return
                                else:
                                    await make_intro.send(embed=embed_4)
                                    x3 = False

                                    def check5(m5):
                                        return m5.channel == make_intro and m5.author == ctx.author

                                    x4 = True
                                    while x4:
                                        hobby = await self.bot.wait_for(
                                            'message', check=check5)
                                        if hobby.content.isdigit():
                                            await make_intro.send(
                                                '```You cannot have a number as a hobby! ```'
                                            )
                                            continue
                                        elif hobby.content == '+END':
                                            return
                                        else:
                                            embed_7 = discord.Embed(
                                                title=
                                                f"{str(name.author.name)}'s INTRO",
                                                color=discord.Colour.blue())
                                            embed_7.set_thumbnail(
                                                url=ctx.author.avatar_url)
                                            embed_7.add_field(
                                                name='NAME',
                                                value=name.content.title(),
                                                inline=False)
                                            print(name.content.title())
                                            embed_7.add_field(
                                                name='AGE',
                                                value=age.content,
                                                inline=False)
                                            embed_7.add_field(
                                                name='GENDER',
                                                value=gender.content.title(),
                                                inline=False)
                                            embed_7.add_field(
                                                name='LOCATION',
                                                value=location.content[0].
                                                upper() + location.content[1:],
                                                inline=False)
                                            embed_7.add_field(
                                                name='HOBBIES',
                                                value=hobby.content[0].upper()
                                                + hobby.content[1:],
                                                inline=False)
                                            k = await intro.send(embed=embed_7)
                                            await k.add_reaction('👋')
                                            await make_intro.send(
                                                f'{ctx.author.mention} ```Your intro has been successfully uploaded in``` {intro.mention}!'
                                            )
                                            x4 = False
                                            db = sqlite3.connect('INTRO.db')
                                            c = db.cursor()
                                            c.execute(
                                                f"CREATE TABLE IF NOT EXISTS info(name TEXT, age INTEGER , gender TEXT , location TEXT, hobbies TEXT, memberid INTEGER , membername TEXT)"
                                            )
                                            c.execute(
                                                f"SELECT name ,age , gender , location , hobbies FROM info WHERE memberid={ctx.author.id} and membername='{ctx.author.name}'"
                                            )
                                            result = c.fetchone()
                                            if result:
                                                c.execute(
                                                    f'UPDATE info SET name ="{name.content}", age={age.content}, gender ="{gender.content}",location="{location.content}",hobbies="{hobby.content[0:len(hobby.content)]}" WHERE memberid={ctx.author.id} and membername="{ctx.author.name}" '
                                                )
                                                db.commit()
                                                db.close()
                                                test = True
                                            else:
                                                c.execute(
                                                    f'INSERT INTO info VALUES ("{name.content}" , {age.content} , "{gender.content}","{location.content}","{hobby.content[0:len(hobby.content)]}", {ctx.author.id} , "{ctx.author.name}")'
                                                )
                                                db.commit()
                                                db.close()

    @commands.command(aliases=['Whois'])
    async def whois(self, ctx, member: discord.Member):
        db = sqlite3.connect('INTRO.db')
        c = db.cursor()
        c.execute(
            f"SELECT name , age , gender , location , hobbies FROM info WHERE memberid={member.id} and membername='{member.name}' "
        )
        result = c.fetchall()
        if result:
            for row in result:
                Name = row[0]
                n = Name.title()
                Age = row[1]
                Gender = row[2]
                g = Gender.title()
                Location = row[3]
                l = Location.title()
                Hobbies = row[4]
                h = Hobbies[0].upper()
                mainh = h + Hobbies[1:len(Hobbies)]
                print(mainh)
                embed = discord.Embed(color=discord.Colour.red())
                embed.set_author(name=f'{member}', icon_url=member.avatar_url)
                embed.add_field(name='Name', value=n, inline=False)
                embed.add_field(name='Age', value=Age, inline=False)
                embed.add_field(name='Gender', value=g, inline=False)
                embed.add_field(name='Location', value=l, inline=False)
                embed.add_field(name='Hobbies', value=mainh, inline=False)
                embed.set_footer(text=f'Exposed by {ctx.author.name}',
                                 icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url=member.avatar_url)
                await ctx.channel.send(embed=embed)
                db.commit()
                db.close()
        else:
            await ctx.channel.send(
                f'{member.mention} does not have intro! HAH nice try {ctx.author.mention}.😂'
            )

    @intro.error
    async def intro_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandOnCooldown):
            await ctx.channel.send(
                ctx.author.mention +
                f' ```chill down lad. You will be able to make an intro again in {round(error.retry_after, 0)} seconds```'
            )

    @commands.command()
    async def END(self, ctx):
        return


async def setup(client):
    await client.add_cog(intro(client))
