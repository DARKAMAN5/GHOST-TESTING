# Originally written by levina on github
# Broadcast function


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as Bot
from config import SUDO_USERS

@Client.on_message(filters.command(["dcast"]))
async def dcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙳𝙲𝙰𝚂𝚃🔥`")
        if not message.reply_to_message:
            await wtf.edit("𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝚂𝚃𝙰𝚁𝚃 𝙳𝙲𝙰𝚂𝚃!")
            return
        lmao = message.reply_to_message.text
        async for dialog in Bot.iter_dialogs():
            try:
                await Bot.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`𝙳𝙲𝙰𝚂𝚃𝙸𝙽𝙶🔥` \n\n**𝚂𝙴𝙽𝚃 𝚃𝙾 ✘** `{sent}` 𝙲𝙷𝙰𝚃𝚂 \n**𝙵𝙰𝙸𝙻𝙴𝙳 𝙸𝙽 ✘** {failed} 𝙲𝙷𝙰𝚃𝚂")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`𝙳𝙰𝚁𝙺𝙲𝙰𝚂𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 🔥` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
