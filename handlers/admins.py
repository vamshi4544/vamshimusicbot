from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from grootmusic import grootmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


ACTV_CALLS = []

@Client.on_message(command(["end"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        grootmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await grootmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("**ʙᴏᴛ ɪsɴ'ᴛ sᴛʀᴇᴀᴍɪɴɢ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ.**")

@Client.on_message(command(["skip"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in grootmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("**❗దాటవేయడానికి 😏 ఏదీ ఆడటం లేదు.**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await grootmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await grootmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        grootmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
