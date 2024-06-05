import logging
from sys import stdout

from modulea.greet import greet

print("1) Ciao.....", __name__, __file__)
greet("World")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# remove all handlers
for handler in logger.handlers[:]:
    logger.removeHandler(handler)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('log.txt')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stdout_handler = logging.StreamHandler(stdout)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
