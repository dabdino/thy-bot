import discord
import os
import asyncio
import datetime
from discord.ext import commands
from config import Config

currentdate = datetime.datetime.now()

# prefix and client assignment
prefix = '.'
client = commands.Bot(
    command_prefix=prefix,
    case_insensitive=True
)

# removes help commmand
client.remove_command("help")

# loads cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# cog commands
@client.command()
async def reloadcog(message, extension):
    if message.author.id != 436894605712293888:
        return
    else:
        client.unload_extension(f"cogs.{extension}")
        msg = await message.channel.send("unloaded cog...")
        asyncio.sleep(1)
        client.load_extension(f"cogs.{extension}")
        await msg.edit(content="loaded cog")


@client.command()
async def loadcog(message, extenstion):
    if message.author.id != 436894605712293888:
        return
    else:
        client.load_extension(f"cogs.{extension}")
        await message.channel.send(content="loaded cog")


# loads status
async def change_status():
    await client.wait_until_ready()

    while not client.is_closed():
        servers = []
        for x in client.guilds:
            servers.append(x)
        activity = discord.Game(name=f"Helping {len(servers)} Servers, Serving Others")
        await client.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(20)


# events

@client.event
async def on_message(message):
    immune = [436894605712293888, 401195259784331284]

    if message.author == client.user:
        return
    if message.author.bot:
        return
        # if user says k
    if message.content == "k" and message.author.id != 436894605712293888:
        await message.channel.send("k")
        # If user says no u
    if "no u" in message.content or "No u" in message.content or "no you" in message.content or "No You" in message.content or "No you" in message.content:
        await message.channel.send("no u")
    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send("Dont DM Me. Only use my commands on a server")
        # Dad part. Make togglable?
    if message.content.startswith("im") and message.author.id not in immune or message.content.startswith("Im") and message.author.id not in immune:
        end = len(message.content)
        await message.channel.send("Hi " + message.content[3:end] + ", Im Dad!")
    if message.content.startswith("I'm") and message.author.id not in immune or message.content.startswith("i'm") and message.author.id not in immune:
        end = len(message.content)
        await message.channel.send("Hi " + message.content[3:end] + ", Im Dad!")
    await client.process_commands(message)


@client.event
async def on_ready():
    number = 0
    print('Logged in as')
    print(client.user.name)
    print("Current date:", currentdate.day, currentdate.month, currentdate.year)
    print("Current Servers Im In:")
    print("------")
    for x in client.guilds:
        number += 1
        print(f"{number}: {str(x)}")
    print('------')


# runs client
client.loop.create_task(change_status())
client.run(Config.TOKEN, reconnect=True, bot=True)
