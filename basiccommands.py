import discord
import random
from discord.ext import commands

colors = [discord.Colour.blue(),
          discord.Colour.orange(),
          discord.Colour.red(),
          discord.Colour.dark_blue(),
          discord.Colour.purple()]

prefix = '.'


class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="help")
    async def _help(self, ctx):
        randcolor = random.choice(colors)
        retstr = "Made with :heart: by Wumbo#0556."
        embed = discord.Embed(
            description=f"**Here are the current commands:**\n \n"
                        f"**`{prefix}help`:** Displays current commands/gives info about those commands\n"
                        f"**`{prefix}crabs`:** Sends a picture of a crab\n"
                        f"**`{prefix}quote`:** Sends a Lovely Quote\n"
                        f"**`{prefix}link`:** Sends the Link to the Bot\n"
                        f"**`{prefix}ping`:** Shows Current Latency/Ping\n \u200b"
                        f"**`{prefix}info`:** Displays Selected User's Info\n"
                        f"**`{prefix}flip`:** A coin is flipped and you choose weither its heads or tails\n"
                        f"**`{prefix}randomchoice`:** Picks a number between the selected numbers\n"
                        f"**`{prefix}roast`:** Roast Selected User\n"
                        f"**`{prefix}discord`:** Sends the discord for the bot\n"
                        f"**`{prefix}clear`:** Clears a selected amount of chats\n"
                        f"**`{prefix}rps`:** Plays a classic Rock, Paper, Scissors game!"
                        f"**`{prefix}recommend`:** Recommend a idea to be added to the bot!",
            colour=randcolor
        )
        embed.add_field(
            name=f"This Bot Is Still In Devolpment! If you wanna join the discord "
                 f"for the bot do {prefix}discord in the proper channel",
            value=retstr)
        await ctx.send(embed=embed)
        print(f"{ctx.author} did .help")

    @commands.command()
    async def link(self, ctx):
        myembed = discord.Embed(
            title="This is the bots invite link:",
            description="https://discordapp.com/api/oauth2/authorize?client_id=585109086383767554&permissions=8&scope=bot",
            color=random.choice(colors)
        )
        await ctx.send(embed=myembed)
        print(f"{ctx.author} did .link")

    @commands.command()
    async def ping(self, ctx):
        myembed = discord.Embed(
            title=f"Pong! {round(self.client.latency * 1000)}ms",
            color=random.choice(colors)
        )
        await ctx.send(embed=myembed)
        print(f"{ctx.author} did .ping")

    @commands.command(name="discord")
    async def discord_(self, ctx):
        myembed = discord.Embed(
            title="Here is my creators discord!",
            description="https://discord.gg/KE3tMA8",
            color=random.choice(colors)
        )
        myembed.add_field(name="If you ever need to contact my creator directly, here is his discord:", value="Wumbo#0556")
        await ctx.send(embed=myembed)

    @commands.command(pass_context=True)
    async def info(self, ctx, user: discord.Member = None):
        if user is not None:
            embed = discord.Embed(
                title=f"{user.display_name}'s Info\n",
                description=f"The users name is: {user.display_name}\n \n"
                            f"The User's ID is: {user.id}\n \n"
                            f"The User's Status is: {user.status}\n \n"
                            f"The User's Highest Role Seems To Be: {user.top_role}\n \n"
                            f"The User joined at: {user.joined_at}\n \n",
                colour=random.choice(colors)
            )
            await ctx.send(embed=embed)
        if user is None:
            user = ctx.author
            embed = discord.Embed(
                title=f"{user.display_name}'s Info\n",
                description=f"The users name is: {user.display_name}\n \n"
                            f"The User's ID is: {user.id}\n \n"
                            f"The User's Status is: {user.status}\n \n"
                            f"The User's Highest Role Seems To Be: {user.top_role}\n \n"
                            f"The User joined at: {user.joined_at}\n \n",
                colour=random.choice(colors)
            )
            await ctx.send(embed=embed)
            # await ctx.send("Please Tag a User To Look At Their Info")
        print(f"{ctx.author} did .info")

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.BadArgument):
            await ctx.send('Could not recognize user')
        if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
            await ctx.send("This command is not working right now")

    @commands.command()
    async def recommend(self, ctx, *, idea):
        print(f"{ctx.author} did .idea")
        myembed = discord.Embed(
            title="You sure you want to recommend (y or n):",
            description=idea,
            color=random.choice(colors)
        )
        await ctx.send(embed=myembed)
        confirmation = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
        if confirmation.content == "y" or confirmation.content == "Y" or confirmation.content == "yes" or confirmation.content == "Yes":
            a = open("/home/ethan/Desktop/Programming/python/Discord bot(5 bots)/main rewrite/cogs/data/recommends.txt", "a")
            a.write(f"{ctx.author} recommended: \n{idea} \n \n")
            a.close()
            await ctx.send("Recommendation sent!")
        elif confirmation.content == "n" or confirmation.content == "N" or confirmation.content == "no" or confirmation.content == "N":
            await ctx.send("Recommendation not sent!")
        else:
            await ctx.send("Invaild reponse, not sending recommendation")

def setup(client):
    client.add_cog(BasicCommands(client))
