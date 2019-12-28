import discord
import random
import os
from discord.ext import commands

colors = [discord.Colour.blue(),
          discord.Colour.orange(),
          discord.Colour.red(),
          discord.Colour.dark_blue(),
          discord.Colour.purple()]

quotes = ["I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to "
          "handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best",
          "Be yourself; everyone else is already taken",
          "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
          "So many books, so little time",
          "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.",
          "A room without books is like a body without a soul.",
          "You've gotta dance like there's nobody watching, Love like you'll never be hurt, Sing like there's nobody "
          "listening, And live like it's heaven on earth.",
          "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
          "You only live once, but if you do it right, once is enough.",
          "Be the change that you wish to see in the world.",
          "In three words I can sum up everything I've learned about life: it goes on.",
          "Don’t walk in front of me… I may not follow Don’t walk behind me… I may not lead Walk beside me… just be "
          "my friend",
          "No one can make you feel inferior without your consent.",
          "If you tell the truth, you don't have to remember anything.",
          "I've learned that people will forget what you said, people will forget what you did, but people will never "
          "forget how you made them feel.",
          "A friend is someone who knows all about you and still loves you.",
          "Always forgive your enemies; nothing annoys them so much.",
          "To live is the rarest thing in the world. Most people exist, that is all."]

crabs = [
    "https://www.washingtonian.com/wp-content/uploads/2018/07/BlueCrabFeat.jpg",
    "https://ewscripps.brightspotcdn.com/dims4/default/d4bfddc/2147483647/strip/true/crop/640x360+0+60/resize/1280x720!/quality/90/?url=https%3A%2F%2Fmediaassets.abcactionnews.com%2Fphoto%2F2018%2F09%2F19%2Fgreen-crabs-generic_1537354298769_97944158_ver1.0_640_480.png",
    "https://scx1.b-cdn.net/csz/news/800/2018/ediblecrabsw.jpg",
    "https://media.mnn.com/assets/images/2018/07/RedCrabWhiteBackground.jpg.653x0_q80_crop-smart.jpg",
    "https://www.peta.org/wp-content/uploads/2013/11/rainbow-crab-5-668x336.jpg?20190103024355",
    "https://nfwp-static.s3.amazonaws.com/uploads/2018/01/1200x900-1309-BC-Jimmy-Sand2-728x420.jpg",
    "https://media.phillyvoice.com/media/images/Blue_Crab.2e16d0ba.fill-735x490.png",
    "https://www.citarella.com/media/catalog/product/cache/1/mobile_image/9df78eab33525d08d6e5fb8d27136e95/0/2/024029200000_01_1.jpg",
    "https://images.newscientist.com/wp-content/uploads/2019/10/22155135/shutterstock_739163554.jpg",
    "https://imagevars.gulfnews.com/2019/07/05/Crab_16bc2f38eb6_large.jpg",
    "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F190911100741-02-ghost-crab-file.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTzr6OdOGz9Xu6vStoLpJUACDl-dNbzwA_HAWCHUI6D6zmMylacQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJooMSRku5_KVQikaOwT91J5nOUtLZ5uE6dQND38dtgCRNrJxB&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaDRqdlzd96DLqI72uYNfHp2q7aN2tOAQjWjVPlN0YfFPLHB5K&s"
]
prefix = '.'


class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def quote(self, ctx):
        myembed = discord.Embed(
            title=random.choice(quotes),
            color=random.choice(colors)
        )
        await ctx.send(embed=myembed)
        print(f"{ctx.author} did .quote")

    @commands.command()
    async def roast(self, ctx, user: discord.User = None):
        print(f"{ctx.author} did .roast")
        if user is None:
            await ctx.send("Please tag a user to roast dumbass")
        elif user.id == 436894605712293888:
            await ctx.send("Dont try to roast my creator")
        elif user == ctx.author:
            await ctx.send("Why are you trying to roast yourself?")
        else:
            if user.id == 585109086383767554:
                await ctx.send("Dont try to roast me stupid")
            else:
                roasts = [
                    f"If {user.display_name}'s brain was dynamite, there wouldn’t be enough to blow your hat off.",
                    f"{user.display_name} is so fucking dumb the asian kid had to pop his ass",
                    f"{user.display_name} family's tree must be a cactus because everyone on it is a prick",
                    f"{user.display_name} is the reason why we created the middle finger",
                    f"I’m jealous of all the people who haven’t met {user.display_name}",
                    f"{user.display_name} is the reason the gene pool needs a lifeguard"
                ]
                choice = random.choice(roasts)
                await ctx.send(choice)

    @commands.command()
    async def randomchoice(self, ctx, small=None, big=None):
        print(f"{ctx.author} did .randomchoice")
        if small is None:
            await ctx.send("Give me numers to choose from")
        if small is not None:
            if big is None:
                await ctx.send(f"Invaild Usage! Usage: `{prefix}randomchoice (minimal) (maximum)`")
            if big is not None:
                try:
                    myembed = discord.Embed(
                        title=f"Random Number Generator!\nSmallest number: `{small}`\nBiggest Number: `{big}`",
                        description=str(random.randint(int(small), int(big))),
                        colour=random.choice(colors)
                    )
                    await ctx.send(embed=myembed)
                except ValueError:
                    await ctx.send("An error has accured")

    @commands.command()
    async def rps(self, ctx):
        print(f"{ctx.author} did .rps")
        embed1 = discord.Embed(
            title=f"Rock, Paper, Scissors",
            description="Please type the choice u want to use! \n \n[1] Rock \n \n[2] Paper \n \n[3] Scissors",
            colour=discord.Colour.dark_blue()
        )
        while 'Wait 1 second':
            game = ["rock", "paper", "scissors"]
            results = ["You Won!", "You Lost!", "A Tie!"]
            bot = random.choice(game)
            await ctx.send(embed=embed1)
            msg = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
            if msg.content.capitalize() == bot.capitalize():
                result = results[2]
                colour = discord.Colour.blue()
            elif msg.content == "rock" and bot == "paper" or msg.content == "Rock" and bot == "paper":
                result = results[1]
                colour = discord.Colour.dark_red()
            elif msg.content == "paper" and bot == "rock" or msg.content == "Paper" and bot == "rock":
                result = results[0]
                colour = discord.Colour.green()
            elif msg.content == "rock" and bot == "scissors" or msg.content == "Rock" and bot == "scissors":
                result = results[0]
                colour = discord.Colour.green()
            elif msg.content == "scissors" and bot == "rock" or msg.content == "Scissors" and bot == "rock":
                result = results[1]
                colour = discord.Colour.dark_red()
            elif msg.content == "scissors" and bot == "paper" or msg.content == "Scissors" and bot == "paper":
                result = results[0]
                colour = discord.Colour.green()
            elif msg.content == "paper" and bot == "scissors" or msg.content == "Paper" and bot == "scissors":
                result = results[1]
                colour = discord.Colour.dark_red()
            else:
                await ctx.send("Please type a valid value! Was the spelling correct?")
                return
            embed2 = discord.Embed(
                title=f"{ctx.message.author.display_name}'s Rock, Paper, Scissors Game!",
                description=f"Bot choice: `{bot.capitalize()}` \n \nYour choice:`{msg.content.capitalize()}` \n \nResult:`{result}`",
                colour=colour
            )
            await ctx.send(embed=embed2)
            return

    @commands.command()
    async def flip(self, message: discord.Message):
        print(f"{message.author} did .flip")
        coin = ["heads", "tails"]
        flipchoice = random.choice(coin)
        while 'Wait 1 second':
            await message.channel.send(f"**`Heads`** or **`Tails`**?")
            msg = await self.client.wait_for('message', check=lambda msg: msg.author == message.author)
            if msg.content == flipchoice:
                await message.channel.send(f"You got it! The answer was {flipchoice}! You get Nothing! ")
                return
            else:
                await message.channel.send(f"Oh no! It was {flipchoice} Try again next time")
                return

    @flip.error
    async def flip_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
            await ctx.send("You ran out of time! oh no")

    @commands.command()                          
    async def crabs(self, ctx):
        crabchoice = random.choice(crabs)
        try:
            #with open(f'/home/ethan/Desktop/Programming/python/Discord bot(5 bots)/main rewrite/cogs/crabs/{picturechoice}', 'rb') as picture:
            #    await ctx.send('Here is a Picture of a Crab!', file=discord.File(picture))
            myembed = discord.Embed(
                title="Here is a picture of a crab!",
                color=random.choice(colors)
            )
            myembed.set_image(url=crabchoice)
            myembed.set_footer(text="If there is any issues with this bot, please contact my creator: Wumbo#0556")
            await ctx.send(embed=myembed)
        except:
            await ctx.send("This command is not working rn")
        print(f"{ctx.author} did .crabs")


def setup(client):
    client.add_cog(FunCommands(client))
