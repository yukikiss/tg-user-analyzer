from telethon import TelegramClient, events
import logging
import datetime
import asyncio
import config


conf = config.get_config()
api_id = conf['api_id']
api_hash = conf['api_hash']
client = TelegramClient('alt', api_id, api_hash)