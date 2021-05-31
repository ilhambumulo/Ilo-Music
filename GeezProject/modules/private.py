import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Halo, saya adalah 𝐈𝐥𝐨-𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 !\n\nSaya adalah Bot Music yang dirancang khusus untuk menemani anda memutar musik dalam grup melalui obrolan suara.\n\n Silahkan anda tekan [disini](https://t.me/infoiam) untuk melihat cara penggunaan hingga info terbaru tentang Bot Music ini.\n\nMasukkan saya dengan [assistant](https://t.me/asistenilomusic) saya kedalam grup anda lalu jadikan admin, dan dengarkan musik sepuasnya!
</b>""",
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

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )



@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Cara Menggunakan BOT 📜", url="https://t.me/infoiam/3"
                    )
                ]
            ]
        ),
    )  

def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️Next', callback_data = "help+2")]
        ]
    elif(pos==len(help)-1):
        url = f"https://t.me/infoiam"
        button = [
            [InlineKeyboardButton("➕ Add me to your Group", url=f"https://t.me/ilomusicbot?startgroup=true")],
            [InlineKeyboardButton(text = '📣 Official Channel', url=f"https://t.me/infoiam"),
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

@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Saya", url="https://t.me/titiktemufams"
                    ),
                    InlineKeyboardButton(
                        "🌿 Owner", url="https://t.me/iamnibng"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""Hai selamat datang✨\n\n Bot Music adalah Bot yang dirancang khusus untuk memutar music secara simple dan mudah.\n Silahkan tambahkan saya dan assistant saya ke grup anda.""",
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

