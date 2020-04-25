import argparse
from gyoji.client import gyoji_client
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

parser = argparse.ArgumentParser(description="CLI for GyojiBot")

parser.add_argument('-t', '--token', help="Token for GyojiBot to log into discord with.")
parser.add_argument('-v', '--verbose', action="store_true", help="Use verbose logging.")

args = parser.parse_args()

token = args.token

verbose_logging = args.verbose

if verbose_logging:
    logger.debug("Using token: %s", token)

client = gyoji_client()

client.run(token)
