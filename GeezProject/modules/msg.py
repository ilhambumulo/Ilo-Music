# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
class Messages():
      START_MSG = "**Haloo 👋 [{}](tg://user?id={})!**\n\n🤖 Saya adalah bot yang dapat memutar musik dalam obrolan suara Grup Telegram.\n\n✅ Send me /help for more info."
      HELP_MSG = [
        ".",
f"""
**Haloo selamat datang di Ilo-Music✨
⚪️ Ilo-Music dapat memutar musik di obrolan suara grup anda.
⚪️ [Ilo-Music Assistant](https://t.me/asistenilomusic)\n\nClick next for instructions**
""",

f"""
**Setting up**
1) Jadikan bot sebagai admin
2) Mulai obrolan suara
3) Cobalah /play [nama lagu] untuk pertama kalinya dari admin
*) Jika userbot bergabung, nikmati musiknya! dan jika tidak, maka tambahkan [Ilo-Music Assistant](https://t.me/asistenilomusic) di grup anda dan coba lagi.
**Commands**
**=>> Memutar Musik 🎧**
- /play: Putar musik menggunakan musik dari youtube
- /play [yt url] : Putar menggunakan yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
**=>> Playback ⏯**
- /player: Buka pengaturan menu dari Assistant
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
- /userbotjoin: Undang [Ilo-Music Assistant](https://t.me/asistenilomusic) Userbot ke grup chat anda
*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
"""
      ]
