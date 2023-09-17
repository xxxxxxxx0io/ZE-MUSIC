import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from AnonXMusic import app

users_list = []

@app.on_message(filters.command(["مين شغل", "شغل", "/play"]))
async def get_last_user(client, message):
    # التحقق مما إذا كان المستخدم قد قام بكتابة الأمر
    if message.from_user.username:
        # إضافة اسم المستخدم والمستخدم إلى قائمة المستخدمين
        users_list.append((message.from_user.username, message.from_user.first_name))
        await message.reply(f"تم تسجيل المستخدم: {message.from_user.first_name} (@{message.from_user.username})",
                            reply_to_message_id=message.message_id)
    else:
        await message.reply("عذرًا، لا يمكنني الوصول إلى اسم المستخدم الخاص بك.", reply_to_message_id=message.message_id)

@app.on_message(filters.command(["مين شغل"]))
async def get_last_user(client, message):
    if users_list:
        # الحصول على آخر مستخدم قام بكتابة الأمر
        last_user = users_list[-1]
        await message.reply(f"الي شغل اهو: {last_user[1]} (@{last_user[0]})",
                            reply_to_message_id=message.message_id)
    else:
        await message.reply("مفيش حد شغل حاجه.",
                            reply_to_message_id=message.message_id)
