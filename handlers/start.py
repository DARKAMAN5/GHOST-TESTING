from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIBVmGsmwYc9XwicImk5Taqj68VcNqOAAINBQAC18VpVSP_OiTpAQIRIgQ")
    await message.reply_text(
        f"""✨ **𝐖𝐄𝐋𝐂𝐎𝐌𝐄 {message.from_user.mention()} !**\n
🔥 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝐂𝐀𝐍 𝐏𝐋𝐀𝐘 𝐌𝐔𝐒𝐈𝐂 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐎𝐏 𝐆𝐑𝐎𝐔𝐏 𝐕𝐎𝐈𝐂𝐄 𝐂𝐇𝐀𝐓 💖.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "༎⃝✨𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐆..༎⃝➤",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("༎⃝💖𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐌𝐄༎⃝➤", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("༎⃝🌸𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒༎⃝➤", callback_data="cbcmds"),
                    InlineKeyboardButton("༎⃝💔𝐂𝐑𝐄𝐀𝐓𝐄𝐑༎⃝➤", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "༎⃝🌺𝐒𝐔𝐏𝐏𝐎𝐑𝐓༎⃝➤", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "༎⃝🥀𝐔𝐏𝐃𝐀𝐓𝐄𝐒༎⃝➤", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **𝐇𝐄𝐋𝐋𝐎** {message.from_user.mention()} !
» **press the button below to read the explanation and see the list of available commands !**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="༎⃝💜𝐁𝐀𝐒𝐈𝐂 𝐆𝐔𝐈𝐃𝐄༎⃝➤", callback_data="cbguide")]]
        ),
    )

@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    delta_ping = time() - start
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"`〘 ♕ ᑭσɳց! ♕ 〙`\n" f"〘🔥`{delta_ping * 1000:.3f} ms`〙")


@Client.on_message(filters.command(["uptime", f"uptime@{BOT_USERNAME}"]))
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**༎⃝💜𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐔𝐒༎⃝➤ ✘\n**
 **༎⃝🔥𝐔𝐏𝐓𝐈𝐌𝐄༎⃝➤ ✘** `{uptime}`\n**
 **༎⃝🌺𝐒𝐓𝐀𝐑𝐓 𝐓𝐈𝐌𝐄༎⃝➤ ✘** `{START_TIME_ISO}`**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "༎⃝🥀𝐔𝐏𝐃𝐀𝐓𝐄𝐒༎⃝➤", url=f"https://t.me/{UPDATES_CHANNEL}"
                   )
                ]
            ]
        )
    ) 
