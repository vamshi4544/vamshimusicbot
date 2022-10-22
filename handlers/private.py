#G-Network Music Projects
#Copyright (C) 2022 By @Groot_Network
#Don't Any Value In This Repo If You Edit Your Github Will Get Banned 😌

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
        photo=f"https://te.legra.ph/file/bb20e1b39e8d7a31f7cbc.jpg",
        caption=f"""**
━━━━━━━━━━━━━━━━━━━━━━━━
😒 𝐖𝐞𝐥𝐜𝐨𝐦𝐞**{message.from_user.mention()} 👋**

😌 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 [{BOT_NAME}](https://t.me/{BOT_USERNAME}), 𝐀 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭.

💗 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐌𝐮𝐬𝐢𝐜...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("🌱❰𝐆𝐫𝐨𝐨𝐭 𝐍𝐞𝐭𝐰𝐨𝐫𝐤❱✨", url=f"https://t.me/Groot_Network"),
           ],[
           InlineKeyboardButton("🌸❰𝐔𝐩𝐝𝐚𝐭𝐞𝐬❱✨", url="https://t.me/RJbr0"),  
           InlineKeyboardButton("👻❰𝐆𝐢𝐭 𝐎𝐰𝐧𝐞𝐫 𝐗𝐃❱✨", url="https://t.me/MyNameIsGroot"),
           ],[
           InlineKeyboardButton("🥀❰𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞❱✨", url="https://t.me/TeluguFriendsClub")
           ]]
           )
     )
    
@Client.on_message(command(["Groot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0c448c9873a3dcb62673a.jpg",
        caption=f"""**🥀🖤 ʸᵒᵘʳ 𝗛𝗘𝗔𝗥𝗧 ⁱˢ 𝗠𝗬 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗜𝗕𝗜𝗟𝗜𝗧𝗬🖤🥀**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "@𝗠𝘆𝗡𝗮𝗺𝗲𝗜𝘀𝗚𝗿𝗼𝗼𝘁", url=f"https://t.me/MyNameIsGroot")
                ]
            ]
        ),
    )
