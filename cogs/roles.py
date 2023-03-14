import discord
from discord.ext import commands
from discord.utils import get


class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def createcolorroles(self, ctx):
        guild = self.client.get_guild(783547639944839178)
        await guild.create_role(name="red", colour=discord.Colour(int('F51720', 16)))
        await guild.create_role(name="skyblue", colour=discord.Colour(int('11A7BB', 16)))
        await guild.create_role(name="yellow", colour=discord.Colour(int('F8D210', 16)))
        await guild.create_role(name="purple", colour=discord.Colour(int('A16AE8', 16)))
        await guild.create_role(name="pink", colour=discord.Colour(int('FFAEBC', 16)))
        await guild.create_role(name="palegreen", colour=discord.Colour(int('2AB67B', 16)))
        await guild.create_role(name="orange", colour=discord.Colour(int('FEA303', 16)))
        await guild.create_role(name="mint", colour=discord.Colour(int('B4F8C8', 16)))
        await guild.create_role(name="gray", colour=discord.Colour(int('B19FF9', 16)))
        await guild.create_role(name="green", colour=discord.Colour(int('31ED31', 16)))
        await guild.create_role(name="cream", colour=discord.Colour(int('FBE7C6', 16)))
        await guild.create_role(name="brightpink", colour=discord.Colour(int('FA26A0', 16)))
        await guild.create_role(name="brightgreen", colour=discord.Colour(int('10BC10', 16)))
        await guild.create_role(name="blue", colour=discord.Colour(int('A0E7E5', 16)))
        await guild.create_role(name="beach", colour=discord.Colour(int('FFD370', 16)))
        await ctx.send("Done.")

    @commands.command()
    async def colors(self, ctx):
        embed = discord.Embed(
            title="Relaxing Waters",
            color=discord.Color.dark_blue()
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/692986387120783415/810774654577803264/Relaxing_Waters.jpg")
        relaxing_waters = await ctx.send(embed=embed)

        embed2 = discord.Embed(
            title="Fiery Volcanoes",
            color=discord.Color.dark_red()
        )
        embed2.set_image(
            url='https://cdn.discordapp.com/attachments/692986387120783415/810774655853002782/Fiery_Volcanoes.jpg')
        fiery_volcanoes = await ctx.send(embed=embed2)

        await relaxing_waters.add_reaction("<:grey_B19FF9:810478374941884416>")
        await relaxing_waters.add_reaction("<:skyblue_11A7BB:810478375318585344>")
        await relaxing_waters.add_reaction("<:blue_A0E7E5:810478374397018123>")
        await relaxing_waters.add_reaction("<:mint_B4F8C8:810478375055130664>")
        await relaxing_waters.add_reaction("<:palegreen_2AB67B:810478375272448110>")

        await fiery_volcanoes.add_reaction("<:red_F51720:810478375180435456>")
        await fiery_volcanoes.add_reaction("<:yellow_F8D210:810478375365378048>")
        await fiery_volcanoes.add_reaction("<:orange_FEA303:810478374941491200>")
        await fiery_volcanoes.add_reaction("<:cream_FBE7C6:810478374896009226>")
        await fiery_volcanoes.add_reaction("<:green_31ED31:810478374942146601>")

    @commands.command()
    async def cosmos(self, ctx):
        embed = discord.Embed(
            title="Colorful Cosmos",
            color=discord.Color.magenta()
        )
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/810782980351983626/810783026756845578/Colorful_Cosmos.jpg')
        cosmos = await ctx.send(embed=embed)

        await cosmos.add_reaction("<:brightpink_FA26A0:810478374777913344>")
        await cosmos.add_reaction("<:brightgreen_10BC10:810478374803341352>")
        await cosmos.add_reaction("<:pink_FFAEBC:810478375164313600>")
        await cosmos.add_reaction("<:beach_FFD370:810478374731644938>")
        await cosmos.add_reaction("<:purple_A16AE8:810478375259996170>")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 810784018953666580:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'grey_B19FF9':
                role = guild.get_role(810471074500182036)
            elif payload.emoji.name == 'skyblue_11A7BB':
                role = guild.get_role(810471062449291296)
            elif payload.emoji.name == 'blue_A0E7E5':
                role = guild.get_role(810471083156176916)
            elif payload.emoji.name == 'mint_B4F8C8':
                role = guild.get_role(810471072746045440)
            elif payload.emoji.name == 'palegreen_2AB67B':
                role = guild.get_role(810471069436870676)
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role:
                member = payload.member
                grey = guild.get_role(810471074500182036)
                skyblue = guild.get_role(810471062449291296)
                blue = guild.get_role(810471083156176916)
                mint = guild.get_role(810471072746045440)
                palegreen = guild.get_role(810471069436870676)
                red = guild.get_role(810471060642332713)
                yellow = guild.get_role(810471064425332756)
                orange = guild.get_role(810471071073304596)
                cream = guild.get_role(810471078090637312)
                green = guild.get_role(810471076140285993)
                brightpink = guild.get_role(810471079503200269)
                brightgreen = guild.get_role(810471081378971668)
                pink = guild.get_role(810471067781038090)
                beach = guild.get_role(810471084918439956)
                purple = guild.get_role(810471065998196755)

                role_list = [grey, skyblue, blue, mint, palegreen, red, yellow, orange, cream, green, brightpink,
                             brightgreen, pink, beach, purple]
                if member:
                    if any(role in role_list for role in member.roles):
                        await member.remove_roles(role)
                        print("removed the role")
                    else:
                        await member.add_roles(role)
                        print('added the role')

                else:
                    print("Member not found.")

            else:
                print("Role not found")

        elif message_id == 810784020375797781:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'red_F51720':
                role = guild.get_role(810471060642332713)
            elif payload.emoji.name == 'yellow_F8D210':
                role = guild.get_role(810471064425332756)
            elif payload.emoji.name == 'orange_FEA303':
                role = guild.get_role(810471071073304596)
            elif payload.emoji.name == 'cream_FBE7C6':
                role = guild.get_role(810471078090637312)
            elif payload.emoji.name == 'green_31ED31':
                role = guild.get_role(810471076140285993)
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role:
                member = payload.member
                grey = guild.get_role(810471074500182036)
                skyblue = guild.get_role(810471062449291296)
                blue = guild.get_role(810471083156176916)
                mint = guild.get_role(810471072746045440)
                palegreen = guild.get_role(810471069436870676)
                red = guild.get_role(810471060642332713)
                yellow = guild.get_role(810471064425332756)
                orange = guild.get_role(810471071073304596)
                cream = guild.get_role(810471078090637312)
                green = guild.get_role(810471076140285993)
                brightpink = guild.get_role(810471079503200269)
                brightgreen = guild.get_role(810471081378971668)
                pink = guild.get_role(810471067781038090)
                beach = guild.get_role(810471084918439956)
                purple = guild.get_role(810471065998196755)

                role_list = [grey, skyblue, blue, mint, palegreen, red, yellow, orange, cream, green, brightpink,
                             brightgreen, pink, beach, purple]
                if member:
                    if any(role in role_list for role in member.roles):
                        await member.remove_roles(role)
                        print("removed the role")
                    else:
                        await member.add_roles(role)
                        print('added the role')

                else:
                    print("Member not found.")

            else:
                print("Role not found")

        elif message_id == 810784037433507840:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'brightpink_FA26A0':
                role = guild.get_role(810471079503200269)
            elif payload.emoji.name == 'brightgreen_10BC10':
                role = guild.get_role(810471081378971668)
            elif payload.emoji.name == 'pink_FFAEBC':
                role = guild.get_role(810471067781038090)
            elif payload.emoji.name == 'beach_FFD370':
                role = guild.get_role(810471084918439956)
            elif payload.emoji.name == 'purple_A16AE8':
                role = guild.get_role(810471065998196755)
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role:
                member = payload.member
                grey = guild.get_role(810471074500182036)
                skyblue = guild.get_role(810471062449291296)
                blue = guild.get_role(810471083156176916)
                mint = guild.get_role(810471072746045440)
                palegreen = guild.get_role(810471069436870676)
                red = guild.get_role(810471060642332713)
                yellow = guild.get_role(810471064425332756)
                orange = guild.get_role(810471071073304596)
                cream = guild.get_role(810471078090637312)
                green = guild.get_role(810471076140285993)
                brightpink = guild.get_role(810471079503200269)
                brightgreen = guild.get_role(810471081378971668)
                pink = guild.get_role(810471067781038090)
                beach = guild.get_role(810471084918439956)
                purple = guild.get_role(810471065998196755)

                role_list = [grey, skyblue, blue, mint, palegreen, red, yellow, orange, cream, green, brightpink,
                             brightgreen, pink, beach, purple]
                if member:
                    if any(role in role_list for role in member.roles):
                        await member.remove_roles(role)
                        print("removed the role")
                    else:
                        await member.add_roles(role)
                        print('added the role')

                else:
                    print("Member not found.")

            else:
                print("Role not found")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 810784018953666580:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'grey_B19FF9':
                role = guild.get_role(810471074500182036)
            elif payload.emoji.name == 'skyblue_11A7BB':
                role = guild.get_role(810471062449291296)
            elif payload.emoji.name == 'blue_A0E7E5':
                role = guild.get_role(810471083156176916)
            elif payload.emoji.name == 'mint_B4F8C8':
                role = guild.get_role(810471072746045440)
            elif payload.emoji.name == 'palegreen_2AB67B':
                role = guild.get_role(810471069436870676)
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                guild = await self.client.fetch_guild(payload.guild_id)
                member = await guild.fetch_member(payload.user_id)
                if member is not None:
                    await member.remove_roles(role)
                    print("Done.")
                else:
                    print("Member not found.")
            else:
                print("Role not found")

        elif message_id == 810784020375797781:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'red_F51720':
                role = guild.get_role(810471060642332713)
            elif payload.emoji.name == 'yellow_F8D210':
                role = guild.get_role(810471064425332756)
            elif payload.emoji.name == 'orange_FEA303':
                role = guild.get_role(810471071073304596)
            elif payload.emoji.name == 'cream_FBE7C6':
                role = guild.get_role(810471078090637312)
            elif payload.emoji.name == 'green_31ED31':
                role = guild.get_role(810471076140285993)
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                guild = await self.client.fetch_guild(payload.guild_id)
                member = await guild.fetch_member(payload.user_id)
                if member is not None:
                    await member.remove_roles(role)
                    print("Done.")
                else:
                    print("Member not found.")
            else:
                print("Role not found")

        elif message_id == 810784037433507840:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'brightpink_FA26A0':
                role = guild.get_role(810471079503200269)
            elif payload.emoji.name == 'brightgreen_10BC10':
                role = guild.get_role(810471081378971668)
            elif payload.emoji.name == 'pink_FFAEBC':
                role = guild.get_role(810471067781038090)
            elif payload.emoji.name == 'beach_FFD370':
                role = guild.get_role(810471084918439956)
            elif payload.emoji.name == 'purple_A16AE8':
                role = guild.get_role(810471065998196755)
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                guild = await self.client.fetch_guild(payload.guild_id)
                member = await guild.fetch_member(payload.user_id)
                if member is not None:
                    await member.remove_roles(role)
                    print("Done.")
                else:
                    print("Member not found.")
            else:
                print("Role not found")


async def setup(client):
    await client.add_cog(Roles(client))
