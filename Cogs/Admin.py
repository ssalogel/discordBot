import logging
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot, log: logging.Logger = None):
        self.bot = bot
        self.logger = log

    async def cog_check(self, ctx: commands.Context):
        return {"moderator", "streamer"}.intersection({x.name for x in ctx.author.roles})

    @commands.command(name='say', help="Makes Parker announce something.")
    async def say(self, ctx: commands.Context, *, text: str):
        channel = [c for c in ctx.guild.channels if "annouce" in c.name].pop()
        await channel.send(f"{text}")
