import logging
import asyncio

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

    @commands.command(description="temperature converter",
                      help="""`!temp 100f` or `!temp 10c`""")
    async def temp(self, ctx: commands.Context, temp: str):
        scale = temp[-1]
        try:
            temp = float(temp.strip()[:-1])
        except ValueError:
            await ctx.send(f"I'm sorry, I didn't understand {temp[:-1]} as a number :(")
            return
        if scale == 'f':
            await ctx.send(f'{round((temp-32)/1.8)}° Celsius')
        elif scale == 'c':
            await ctx.send(f'{round(temp*1.8)+32}° Fahrenheit')
        else:
            await ctx.send("I did not understand the scale you used :(")

    @commands.command(description="ask Parker 2.0 to remind you of something",
                      help="""You can ask Parker to remind you of something:
                      `!remind 1.5h remind me to do the dishes`
                      with time either in hours (ex: 2h), minutes (ex: 2.5m) or seconds (ex: 180s)
                      """)
    async def remind(self, ctx: commands.Context, time: str, *, message: str):
        time = time.lower()
        if time[-1] not in ['h', 'm', 's', 'min', 'sec']:
            await ctx.send(f"I'm sorry, I don't understand {time} as a timing :(")
            return
        try:
            timer = float(time[:-1])
        except ValueError:
            await ctx.send(f"I'm sorry, I didn't understand {time[:-1]} as a number :(")
            return
        if time[-1] == 'h':
            timer *= 60 * 60
        elif time[-1] == 'm':
            timer *= 60
        await ctx.message.add_reaction('👍')
        await asyncio.sleep(timer)
        await ctx.send(f"{ctx.author.mention}: {message}")
