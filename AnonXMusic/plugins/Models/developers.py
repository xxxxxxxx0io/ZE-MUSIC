import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randi
                
                
@app.on_message(
    command(["مطور زد إي","المطورين","مطورين","مطورين زد إي"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين زد إي ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐌𝐎𝐃𝐘⌯►", url=f"https://t.me/UP_UO"), 
                 ],[
                    InlineKeyboardButton(
                        "𝐁𝐀𝐑", url=f"https://t.me/UI_OS"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 ⌝⚡", url=f"https://t.me/UI_XB"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مودي الهيبه","مودي","المطور","مبرمج","MODY","mody" ,"المطور مودي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("UP_UO")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["ي٠ مودي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("UP_UO")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["بوت حذف"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("XSCIBOT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**يلا غور احذف يعم دانت بارد😂**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["مساعدة"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""**⩹⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس مانجا\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐌𝐎𝐃𝐘⌯‹", url=f"https://t.me/UP_UO"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄⌝⚡", url=f"https://t.me/UI_XB"),
                ],

            ]

        ),

    )



    