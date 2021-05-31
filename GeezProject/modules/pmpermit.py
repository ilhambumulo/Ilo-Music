from pyrogram import filters
from pyrogram.types import Message

from GeezProject.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Halo, Saya adalah Layanan Asisten Musik yang siap menemani anda memutar musik didalam obrolan suara.\n\n ◈ Silahkan pergi ke channel @infoiam untuk melihat info terbaru tentang musik bot ini, atau bisa hubungi ke @iamnibng jika terjadi masalah pada bot music.\n\n ❗️ Attention:\n ◈  Jangan spam chat kesini, karna akan mengakibatkan akun anda teblokir oleh asisten!\n\n 📣 JIKA ASSISTANT TIDAK BISA DIUNDANG, SILAHKAN KETIK /userbotjoin DIDALAM GRUP ANDA.\n\n 📣 Channel Support : @infoiam\n 🌿 Owner : @iamnibng",
    )
    return
