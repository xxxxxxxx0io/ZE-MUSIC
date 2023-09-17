import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from AnonXMusic import app


@app.on_message(filters.voice & filters.command(["مين شغل"]))
async def whose_job(client, message):
    song_info = message.voice
    performer = song_info.performer
    if performer:
        await message.reply(f"الشخص الذي شغل هذه الأغنية هو  {performer}.")
    else:
        await message.reply("مفيش أغنية شغالة أصلاً يا صحبي.")