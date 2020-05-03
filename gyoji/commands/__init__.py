import logging
from logging import NullHandler

formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

log = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.setLevel(logging.DEBUG)
log.addHandler(handler)
