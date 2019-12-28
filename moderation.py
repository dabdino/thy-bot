import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="kick", pass_context=True)
    @has_permissions(manage_roles=True, ban_members=True)
    async def _kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} kicked")

    @_kick.error
    async def kick_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send(text)

    @commands.command(name="clear")
    @has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount=5):
        print(f"{ctx.author} did .clear")
        try:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"{amount} messages cleared!")
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=1)
        except:
            await ctx.send(
                "An error has occured! "
                "You may not have the permissions to execute this command or I dont have permissions to do this command")

    @_clear.error
    async def clear_error(self, error, ctx):
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            await ctx.send(f"Sorry {ctx.author.mention}, you do not have permissions to do that!")


def setup(client):
    client.add_cog(Moderation(client))
