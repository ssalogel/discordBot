import logging

from discord.ext import commands
from random import choice
from Utils.DiceParser import DiceParser


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot, log: logging.Logger = None):
        self.bot = bot
        self.logger = log
        self.dice_parser = DiceParser()

    @commands.command(name="ping", description="pong!", brief="pong!")
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

    @commands.command(aliases=['dice'], description="Roll a dice, any dice! `!roll #d# + #`", brief="Roll a dice, any dice!",
                      help="to roll two 6 sided dice and a 20 sided dice, plus 4, write '!roll 2d6 + 1d20 + 4'")
    async def roll(self, ctx: commands.Context, dice_expr: str):
        await ctx.send(f"You rolled : {self.dice_parser.parse_expr(dice_expr)[-1]} !")
