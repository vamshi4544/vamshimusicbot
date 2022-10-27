import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, BOT_USERNAME
from config import BOT_NAME
from config import BOT_USERNAME

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/dbb9fe2d8746340eec9b1.jpg",
        caption=f"""**
━━━━━━━━━━━━━━━━━━━━━━━━
😒 𝐖𝐞𝐥𝐜𝐨𝐦𝐞**{message.from_user.mention()} 👋**

😌 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 [{BOT_NAME}](https://t.me/{BOT_USERNAME}), 𝐀 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭.


💐 𝐅𝐞𝐞𝐥 𝐅𝐫𝐞𝐞 𝐓𝐨 🕊️ 𝐀𝐝𝐝 𝐌𝐞 𝐢𝐧 𝐘𝐨𝐮𝐫
𝐆𝐫𝐨𝐮𝐩, 🌺 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 ❥︎ 𝐒𝐮𝐩𝐞𝐫 𝐇𝐢𝐠𝐡
𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 🌷 ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("🎗️❰🇸‌🇦‌🇮‌ 🇰‌🇺‌🇲‌🇦‌🇷‌❱✨", url=f"https://t.me/+wNQjyrs1GaAwZjVl"),
           ],[
           InlineKeyboardButton("🌸❰𝐔𝐩𝐝𝐚𝐭𝐞𝐬❱✨", url="https://t.me/Fake_Friendship_Fake_Smiles"),
           ]]
           )
     )
    
@Client.on_message(command(["Groot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/8fcabe7ad93f3ece32408.jpg",
        caption=f"""**)
                ]
            ]
        )
    )
