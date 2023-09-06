import asyncio
from pyrogram import filters, Client
from AnonXMusic import app
from AnonXMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)
from AnonXMusic.core.call import Anonx
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped

@app.on_message(filters.regex("^مين في الكول$|^مين ف الكول$|^مين في كول$"))
async def strcall(client, message):
    assistant = await group_assistant(AnonX,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./assets/mody.mp3"), stream_type=StreamType().pulse_stream)
        text="🔔 الاعضاء المتواجدين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut=f"٭{participant.volume}٭يتحدث 🗣٭"
            else:
                mut="٭ساكت 🔕٭"
            user = await client.get_users(participant.user_id)
            print(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"عمووووو الكول مش مفتوح اصلااا\n❌")
    except AlreadyJoinedError:
        text="🔔 الاعضاء المتواجدين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut=f"٭{participant.volume}٭يتحدث 🗣٭"
            else:
                mut="٭ساكت 🔕٭"
            user = await client.get_users(participant.user_id)
            print(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"
        await message.reply(f"{text}")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n❌")
        
        
#المطور الهيبه مودي

#𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮

# ســورس زد إي 

# 🔥← المطور :  @UP_UO 

# 🐉← القناه  : @UI_XB

# 💨← جروب : @UI_OS

# 🤖← بوتي : @XBTOBOT