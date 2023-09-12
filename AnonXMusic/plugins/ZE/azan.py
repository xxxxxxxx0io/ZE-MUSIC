#الكود دا بلحب محتاج بس ناس تدع انا و ايرور نعدي السنه دي علي خير
#يوزري @PTPPE
#يزور البولبول @E_Z_9
#يوزر ايرور @S4ASA
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from AnonXMusic import app
from datetime import datetime
import requests
import pytz
from AnonXMusic.core.call import Anony
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonXMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)

adox = pytz.timezone('Africa/Cairo')

chat = []

@app.on_message(filters.text & ~filters.private, group = 20)
async def azaan(c, msg):
  if msg.text == "تفعيل الاذان":
    if msg.chat.id in chat:
      return await msg.reply_text("- الاذان متفعل اصلا يصحبي")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("تم تفعيل الاذان")
  elif msg.text == "تعطيل الاذان":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("تم تعطيل الاذان")
    else:
      return await msg.reply_text("- الاذان متعطله اصلا يصحبي")
           
async def kill():
  for i in chat:
    await Anony.force_stop_stream(i)


async def play(i):
  assistant = await group_assistant(Anony,i)
  file_path = "./AnonXMusic/assets/azan.mp3"
  stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
  try:
      await assistant.join_group_call(
           i,
           stream,
           stream_type=StreamType().pulse_stream,
      )
  except NoActiveGroupCall:
    try:
        await Anony.join_assistant(i,i)
    except Exception as e:
       await app.send_message(i,f"{e}")
  except TelegramServerError:
    await app.send_message(i,"اسف في شوين مشاكل في سرفر التلجرام")
  except AlreadyJoinedError:
    await kill()
    try:
        await assistant.join_group_call(
           i,
           stream,
           stream_type=StreamType().pulse_stream,
        )
    except Exception as e:
        await app.send_message(i,f"{e}")

      
#موعيد الاذان وخدها من ايرور عشان هوا واحد هكور      
def prayer_time():
   try:
       prayer = requests.get(f"http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0")
       prayer = prayer.json()
       fajr = datetime.strptime(prayer['data']['timings']['Fajr'], '%H:%M').strftime('%I:%M %p')
       dhuhr = datetime.strptime(prayer['data']['timings']['Dhuhr'], '%H:%M').strftime('%I:%M %p')
       asr = datetime.strptime(prayer['data']['timings']['Asr'], '%H:%M').strftime('%I:%M %p')
       maghrib = datetime.strptime(prayer['data']['timings']['Maghrib'], '%H:%M').strftime('%I:%M %p')
       isha = datetime.strptime(prayer['data']['timings']['Isha'], '%H:%M').strftime('%I:%M %p')
       if datetime.now(adox).strftime('%I:%M %p') == fajr:
         return "الفجر 🕊❤", "https://t.me/FU_CK_LOVE6/692"
       elif datetime.now(adox).strftime('%I:%M %p') == dhuhr:
         return "الظهر 🕊❤", "https://t.me/FU_CK_LOVE6/693"
       elif datetime.now(adox).strftime('%I:%M %p') == asr:
         return "العصر 🕊❤", "https://t.me/FU_CK_LOVE6/694"
       elif datetime.now(adox).strftime('%I:%M %p') == maghrib:
         return "المغرب 🕊❤", "https://t.me/FU_CK_LOVE6/695"
       elif datetime.now(adox).strftime('%I:%M %p') == isha:  
         return "العشاء 🕊❤", "https://t.me/FU_CK_LOVE6/696" 
   except Exception as e:
       asyncio.sleep(5)
       print(e)        
      
async def azan():
  while not await asyncio.sleep(2):
    if prayer_time():
     prayer = prayer_time()
     await kill()
     for i in chat:
       await app.send_message(i, f"حان الان وقت اذان {prayer}")
       await play(i)
     await asyncio.sleep(174)
     await kill()
#بحبك في الله اوعا تنسي تدعي لينيا واذكر المصدر يا ايوها الخماط بهزر معاك كلنا واحد مفيش حاجه اسمها بتسرق التلي كلو بيسرق❤
