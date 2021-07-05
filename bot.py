import logging
import discord

from localconfig import token
from discord.ext import commands
from Cogs.Misc import Misc

logger = logging.getLogger("discord.bot")

bot = commands.Bot(command_prefix="!", fetch_online_members=False, case_insensitive=True,
                   activity=discord.Activity(type=discord.ActivityType.watching, name="for !help"))


def start_logging():
    syslogger = logging.getLogger('discord')
    syslogger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename="./logs/discordSys.log", encoding='utf-8', mode='a')
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
    handler.setFormatter(formatter)
    syslogger.addHandler(handler)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename="./logs/discordClient.log", encoding='utf-8', mode='a')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord!')
    start_logging()


if __name__ == '__main__':
    bot.add_cog(Misc(bot, logger))
    bot.run(token)
