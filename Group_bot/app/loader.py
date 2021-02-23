from os import environ

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(environ.get("bot_token"))
dp = Dispatcher(bot, storage=storage)
