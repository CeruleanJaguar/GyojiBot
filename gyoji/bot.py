from discord.ext import commands

import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


@commands.command(name='submit')
async def submit_slohyo(ctx, opponent: commands.MemberConverter):
    author = ctx.author
    await ctx.send("User {} is submitting a slohyo for their bout against {}".format(author, opponent))
    # TODO: Implement direct messaging logic, filling out of the slohyo form
    pass
