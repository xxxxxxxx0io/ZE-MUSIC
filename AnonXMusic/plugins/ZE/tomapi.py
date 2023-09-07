import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("ze")
    
)
async def ze_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس ze \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𝐌𝐎𝐃𝐘", url=f"https://t.me/UP_UO"),
                    InlineKeyboardButton(
                        "𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/UI_OS"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝⚡", url=f"https://t.me/UI_XB"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def ze_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━★⊷⌯⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝⌯⊶★━⩺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━★⊷⌯⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def ze_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="tommm")],
            [InlineKeyboardButton("𝐌𝐎𝐃𝐘", url=f"https://t.me/UP_UO"),
             InlineKeyboardButton("𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/UI_OS")],
            [InlineKeyboardButton("★⌞ 𝐙𝐄 • 𝐒𝐎𝐔𝐑𝐂𝐄 ⌝⚡", url=f"https://t.me/UI_XB")],
        ]
    ))

