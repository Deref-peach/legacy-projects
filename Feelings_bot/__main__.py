import os
import asyncio
import argparse

from dotenv import find_dotenv, load_dotenv
from telethon import TelegramClient, events

from feelins_bot.args import file
from feelins_bot.tools import *

load_dotenv(find_dotenv())

api_id = os.environ.get("api_id")
api_hash = os.environ.get("api_hash")

with TelegramClient('anon', api_id, api_hash) as client:

    hub = Github_handler()

    @client.on(events.NewMessage(outgoing=True, pattern=r'.paste'))
    async def handler(event):
        # Say "!pong" whenever you send "!ping", then delete both messages
        m = await event.respond('!pong')
        await asyncio.sleep(5)
        await client.delete_messages(event.chat_id, [event.id, m.id])

    # client.loop.run_until_complete(client.send_message(
    #     'https://t.me/rudepython', 'Я родился'))

    @client.on(events.NewMessage(outgoing=True, pattern=r'exit'))
    async def exit_handler(event):
        raise SystemExit

    @client.on(events.NewMessage(outgoing=True, pattern=r'new_repo'))
    async def new_repo_handler(event):
        parser = argparse.ArgumentParser()
        parser.add_argument('name', type=str)
        parser.add_argument('priv', type=bool)
        parser.add_argument('description', type=str)
        parser.add_argument('ret', type=bool, default=True)
        args = parser.parse_args([])

        repo = await hub.create_repo()
        if args.ret:
            await event.respond(repo)
        client.delete_messages(event.chat_id, [event.id])

    @client.on(events.NewMessage(outgoing=True, pattern=r'!books'))
    async def book_handler(event):
        await event.respond('https://yadi.sk/d/H-00n-UG3RSQem')
        client.delete_messages(event.chat_id, [event.id])
    # @client.on(events.NewMessage(outgoing=True, pattern=r'del_repo'))
    # async def del_repo_handler(event):
    #     repo = await hub.delete_repo()
    #     client.delete_messages(event.chat_id, [event.id])

    @client.on(events.NewMessage(outgoing=True, pattern=r'!json'))
    async def json_handler(event):
        await event.respond(prettiefer())
        client.delete_messages(event.chat_id, [event.id])

    client.run_until_disconnected()
