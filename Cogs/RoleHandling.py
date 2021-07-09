from typing import Dict

from discord.ext import commands
from discord.utils import get
from localconfig import pronouns, position


async def changeRole(ctx: commands.Context, choice: str, category: Dict[str, int]):
    if choice in category:
        choiceID = category[choice]
        role_remove = [x for x in ctx.author.roles if x.id in category.values()]
        role = get(ctx.guild.roles, id=choiceID)
        for r in role_remove:
            await ctx.author.remove_roles(r)
        await ctx.author.add_roles(role)
        await ctx.message.add_reaction('👍')
    else:
        await ctx.send(ctx.command.help)


async def toggleRole(ctx: commands.Context, choice: str, category: Dict[str, int]):
    if choice in category:
        roles = {x.id:x for x in ctx.author.roles}
        choiceID = category[choice]

        if choiceID in roles:
            await ctx.author.remove_roles(roles[choiceID])
        else:
            await ctx.author.add_roles(get(ctx.guild.roles, id=choiceID))
        await ctx.message.add_reaction('👍')

    else:
        await ctx.send(ctx.command.help)


class RoleHandling(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["pronouns"], description="To get a role denoting your pronouns!", help="""
       To toggle a pronoun, please answer with "!pronoun #" where # is the number of your choice or the first element
       of the pronoun (ex: `!pronoun 2` or `!pronoun ze`:          

           1. they/them
           2. ze/zem/zir
           3. she/her
           4. he/him
           5. no pronoun
           6. ne/nem
           7. xie/xir
           8. any pronoun

       You can have as many or as few of these choices as you want :)
       If your prefered pronouns aren't on the list, I'm sorry. ping @ssalogel and they'll fix it!
       """, brief="To select your pronoun(s)")
    async def pronoun(self, ctx: commands.Context, pronoun: str):
        pronoun = pronoun.lower()
        await toggleRole(ctx, pronoun, pronouns)

    @commands.command(name="hire", description="To get a role in the team!", help="""
       To pick your responsabilities, go "!hire <position>" like "!hire thief" with any of the following positions:\n
           Hacker
           Hitter
           Grifter
           Thief
           Mastermind
           Client
           Forger
           Fixer
           Ally
           Maker
       """, brief="to get hired!")
    async def hire(self, ctx: commands.Context, choice: str):
        choice = choice.capitalize()
        await changeRole(ctx, choice, position)
