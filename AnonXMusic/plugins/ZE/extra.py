import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from asyncio import gather
from strings.filters import command
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus

@app.on_message(filters.command(["تلغراف", "تلغراف ميديا", "ميديا"]) & ~BANNED_USERS)
async def telegraph(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("🤕 ¦ الرد على ملف وسائط مدعوم\n• حط صوره و اكتب عليها 00")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("غير مدعوم!!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"<b>• الــرابـط:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🦕 ¦ افـتح الـرابـط", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="🧚🏻‍♀️️ ¦ مشـاركه الـرابـط", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
            ]
        )
    )
    finally:
        os.remove(download_location)
    
@app.on_message(filters.command(["المالك"]))
async def creator(c,msg):
    x = []
    async for m in app.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       lol = await app.get_users(int(x[0]))
       lol = await app.get_owner_bio(bio) 
       if lol.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await msg.reply_photo(photo.file_id,caption=f"᥆ꪝᥒ꧖ᖇ | - {lol.mention} 🦕\n\nႦᎥ᥆ | - {lol.bio} 🦕",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(lol.first_name, url=f"https://t.me/{lol.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await msg.reply_text(f"᥆ꪝᥒ꧖ᖇ | - {lol.mention} 🦕\n\nႦᎥ᥆ | - {lol.bio} 🦕", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(lol.first_name, url=f"https://t.me/{lol.username}")],]))
    else:
        await msg.reply_text("الاك محذوف يقلب")
