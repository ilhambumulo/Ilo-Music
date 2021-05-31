import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 Saya adalah bot yang dapat memutar musik dalam obrolan suara Grup Telegram.\n\n✅ Ketik /help untuk info lainnya."
      HELP_MSG = [
        ".",
f"""
**Hai 👋 Selamat datang di Ilo-Music

⚪️ Ilo-Music dapat memutar music di obrolan suara grup anda.

⚪️ [Ilo-Music Assistant](https://t.me/asistenilomusic)\n\nKlik next untuk instruksinya**
""",

f"""
**Setting up**

1) Jadikan bot sebagai admin
2) Mulai obrolan suara
3) Ketik /play [judul lagu] untuk pertama kalinya dari admin
*) Jika userbot bergabung, nikmati musiknya! dan jika tidak, tambahkan [Ilo-Music Assistant](https://t.me/asistenilomusic) di grup anda dan coba lagi.
**Commands**

**=>> Memutar Musik 🎧**

- /play: Putar musik menggunakan musik dari youtube
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist
""",

f"""
**=>> More tools 🧑‍🔧**

- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite [Ilo-Music Assistant](https://t.me/asistenilomusic) Userbot to your chat

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
"""
      ]
