#G-Network Music Projects
#Copyright (C) 2022 By @Groot_Network

import requests
from pyrogram import idle
from pyrogram import Client as Bot

from groot import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
run()
idle()
