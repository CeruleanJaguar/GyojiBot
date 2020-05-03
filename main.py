import argparse
import os
from gyoji.bot import gyoji_bot
import logging


parser = argparse.ArgumentParser(description='CLI for GyojiBot')

parser.add_argument('-t', '--token', required=True, help='Token for GyojiBot to log into discord with.')
parser.add_argument('-v', '--verbose', action='store_true', help='Use verbose logging.')


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

args = parser.parse_args()

token = args.token

verbose_logging = args.verbose

if verbose_logging:
    logger.debug('Using token: %s', token)

for filename in os.listdir('./gyoji/commands'):
    if filename.endswith('.py') and filename != '__init__.py':
        gyoji_bot.load_extension(f'gyoji.commands.{filename[:-3]}')

gyoji_bot.run(token)
