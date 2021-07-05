from discord.ext import commands
from discord.utils import get
from localconfig import pronouns

class RoleHandling(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="pronoun", description="To get a role denoting your pronouns!", help="""
       To select your pronouns, please answer with "!pronoun #" where # is the number of your choice or the first element
       of the pronoun (ex: `!pronoun 2` or `!pronoun ze`:          

           1. they/them
           2. ze/zem/zir
           3. she/her
           4. he/him
           5. no pronoun
           6. ne/nem
           7. xie/xir
           8. any pronoun

       If your prefered pronouns aren't on the list, I'm sorry. ping @ssalogel and they'll fix it!
       """, brief="To select your pronoun(s)")
    async def pronoun(self, ctx: commands.Context, pronounNumber):
        pronoun = pronounNumber.lower()
        if pronoun in pronouns.keys():
            pronounID = pronouns[pronoun]
            role_remove = [x for x in ctx.author.roles if x.id in pronouns.values()]
            role = get(ctx.guild.roles, id=pronounID)
            for r in role_remove:
                await ctx.author.remove_roles(r)
            await ctx.author.add_roles(role)
        else:
            await ctx.send_help()

