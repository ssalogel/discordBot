import logging

from discord.ext import commands
from random import choice


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot, log: logging.Logger = None):
        self.bot = bot
        self.logger = log

    @commands.command(name="ping", description="pong!",
                 brief="pong!")
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

    @commands.command(name="source", description="If you want to know how I work, this is it :)",
                 brief="Here is me!!")
    async def source(self, ctx: commands.Context):
        await ctx.send("<https://github.com/ssalogel/discord-bot>\nfeel free to @ssalogel with questions!")

    @commands.command(name="choose", description="When you can't pick, Bot can do for you!",
                 brief="When you can't pick, Bot can do for you!")
    async def choose(self, ctx: commands.Context, *choices: str):
        await ctx.send(choice(choices))
