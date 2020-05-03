import discord
from discord.ext import commands
from gyoji import log

gyoji_bot = commands.Bot(command_prefix='Honorable GyojiBot, ')

@gyoji_bot.command(
    hidden = True
)
async def load(ctx, extension: str):
    log.info(f'Loading extension: {extension}')
    gyoji_bot.load_extension(extension)


@gyoji_bot.command(
    hidden = True
)
async def unload(ctx, extension: str):
    log.info(f'Unoading extension: {extension}')
    gyoji_bot.unload_extension(extension)

@gyoji_bot.command(
    hidden = True
)
async def reload(ctx, extension: str):
    log.info(f'Reloading extension: {extension}')
    gyoji_bot.reload_extension(extension)

@gyoji_bot.event
async def on_ready():
    log.info("Ready")
