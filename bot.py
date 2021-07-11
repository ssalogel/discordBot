import logging
import discord

from os import listdir, path
from random import choice
from localconfig import token
from discord.ext import commands
from Cogs.Misc import Misc
from Cogs.RoleHandling import RoleHandling

logger = logging.getLogger("discord.bot")


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", fetch_online_members=False, case_insensitive=True, intents=intents,
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


@bot.event
async def on_member_join(member: discord.Member):
    channel = member.guild.system_channel
    await channel.send(f"Hi and Welcome {member.mention}! You can look in {bot.get_channel(709178518482976860)} for "
                       f"rules and how to get roles attributed :)\nFeel free to ask if you have any questions!")
    await channel.send(file=get_welcome_gif())


def get_welcome_gif() -> discord.File:
    gif_dir = "./assets/welcomeGifs"
    gifs = choice(listdir(gif_dir))
    gifpath = path.join(gif_dir, gifs)
    with open(gifpath, 'rb') as fd:
        return discord.File(fd)


if __name__ == '__main__':
    bot.add_cog(RoleHandling(bot))
    bot.add_cog(Misc(bot, logger))
    bot.run(token)
