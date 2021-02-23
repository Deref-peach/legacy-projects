from os import getenv

from dotenv import find_dotenv, load_dotenv
from vkwave import SimpleLongPollBot

load_dotenv(find_dotenv())

bot = SimpleLongPollBot(token=getenv("TOKEN"))
