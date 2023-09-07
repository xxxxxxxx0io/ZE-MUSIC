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
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين زد إي","المطورين","مطورين","مطورين ze"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين ze ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐌𝐎𝐃𝐘 ", url=f"https://t.me/UP_UO"), 
                 ],[
                    InlineKeyboardButton(
                        "ρ᥆kᥱꪔ᥆ꪀ", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "𝐶𝑅𝐼𝑆𝑇𝐼𝑁", url=f"https://t.me/dr_zeiss"),
                    InlineKeyboardButton(
                        "ꪔᥲ️ꪀ᥆᥆", url=f"https://t.me/C1_I_I"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝⚡", url=f"https://t.me/UI_XB"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["السورس","زد إي","سورس","سورس زد إي","Ze","ZE"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("UI_XB")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**", 
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
    command(["ZE SOURCE","SOURCE ZE","Source Ze","Ze Source","ZE source","Source ZE"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("UI_XB")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**", 
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
    command(["الدعم","جروب الدعم","دعم","جروب دعم","الجروب","البار"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("UI_OS")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**", 
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
    command(["الهيبه مودي","الهيبه","مودي","mody","Mody"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("UP_UO")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**", 
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
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""**⩹⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس ze\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐌𝐎𝐃𝐘", url=f"https://t.me/UP_UO"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝⚡", url=f"https://t.me/UI_XB"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""**⩹⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس ze\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐌𝐎𝐃𝐘", url=f"https://t.me/UP_UO"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝⚡", url=f"https://t.me/UI_XB"),
                ],

            ]

        ),

    )



    
