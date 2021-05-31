import logging
from GeezProject.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Cara Menggunakan BOT 📜", url="https://t.me/infoiam/3")
                  ],[
                    InlineKeyboardButton(
                        "🌿 Owner", url="https://t.me/iamnibng"
                    ),
                    InlineKeyboardButton(
                        "📷 Instagram", url="https://instagram.com/ilhambumulo_"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 Ilo-Music is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Group Chat", url=f"https://t.me/titiktemufams"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️Next', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/infoiam"
        button = [
            [InlineKeyboardButton("➕ Add me to your Group", url=f"https://t.me/ilomusicbot?startgroup=true")],
            [InlineKeyboardButton(text = '📲 Updates', url=f"https://t.me/infoiam"),
             InlineKeyboardButton(text = '💬 Group Chat', url=f"https://t.me/titiktemufams")],
            [InlineKeyboardButton(text = '🌿 Owner', url=f"http://t.me/iamnibng")],
            [InlineKeyboardButton(text = '◀️Undo', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️Undo', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️Next', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Haloo! Saya bisa memutar musik di Obrolan Suara Grup anda.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Klik disini untuk bantuan", url=f"https://t.me/ilomusicbot?start"
                    )
                ]
            ]
        ),
    )

