import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from grootmusic.grootmusic import client as grootmusic
from config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`𝗕𝗿𝗼𝗮𝗱𝗖𝗮𝘀𝘁 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 ...`")
        if not message.reply_to_message:
            await wtf.edit("**__𝗥𝗲𝗽𝗹𝘆 𝗼𝗻 𝗠𝘀𝗴  ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in grootmusic.iter_dialogs():
            try:
                await grootmusic.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗶𝗻𝗴` \n\n**𝗦𝗲𝗻𝗱 𝗧𝗼:** `{sent}` 𝗖𝗵𝗮𝘁𝘀 \n**𝗙𝗮𝗶𝗹𝗲𝗱 𝗜𝗻:** {failed} 𝗖𝗵𝗮𝘁𝘀")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`𝗚𝗰𝗮𝘀𝘁 𝗦𝘂𝗰𝗰𝗲𝘀` \n\n**𝗦𝗲𝗻𝗱 𝘁𝗼:** `{sent}` 𝗖𝗵𝗮𝘁 \n**𝗙𝗮𝗶𝗹𝗲𝗱 𝗜𝗻:** {failed} 𝗖𝗵𝗮𝘁𝘀")
