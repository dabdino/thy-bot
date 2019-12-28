import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = commands.UserInputError

        if isinstance(error, discord.ext.commands.errors.MissingRole):
            await ctx.send("You do not have permissions to do this command")
        if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
            await ctx.send("Either I or You dont have permission to do this command")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Thats not a command! Do `.help` for the command list")
        if isinstance(error, ignored):
               return



def setup(client):
    client.add_cog(Events(client))
