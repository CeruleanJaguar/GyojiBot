import discord
import logging


formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')


class gyoji_client(discord.Client):

    def __init__(self):
        self.log = logging.getLogger()
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(formatter)
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(self.handler)

    async def on_ready(self):
        self.log.info('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        self.log.info('Message from {0.author}: {0.content}'.format(message))
