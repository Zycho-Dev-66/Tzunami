from telethon import events
from time import sleep
from datetime import datetime
from html_telegraph_poster.upload_images import upload_image
import config as config
import base.client as ub

API_ID = config.API_ID
API_HASH = config.API_HASH
SESSION = config.SESSION
COMMAND_HANDLER = config.COMMAND_HANDLER
LOGGER_ID = config.LOGGER_ID
ALIVE_NAME = config.ALIVE_NAME
ALIVE_PIC = config.ALIVE_PIC

client = ub.client
cmdping = COMMAND_HANDLER+ 'ping'
cmdatt = COMMAND_HANDLER+ 'attention'
cmdalert = COMMAND_HANDLER+ 'alert'

@client.on(events.NewMessage(outgoing=True,pattern=r''+cmdping))
async def ping(event):
    try:
        try:
            start = datetime.now()
            chat = await event.get_chat()
            end = datetime.now()
            pingms = (end-start).microseconds / 1000
            await client.edit_message(event.message,"pong! I'm awake!\n{} ms".format(pingms))
        except AttributeError:
            pass
    except:
        pass

@client.on(events.NewMessage(outgoing=True,pattern=r''+cmdalert))
async def alert(event):
    try:
        chat = await event.get_chat()
        await client.edit_message(event.message,"Alert! Reported to @Zycho_66!")
    except:
        pass

@client.on(events.NewMessage(outgoing=True,pattern=r''+cmdatt))
async def attention(event):
    try:
        chat = await event.get_chat()
        await client.edit_message(event.message,"""**Battalion Attetion!**\n
Tzunami Spam Squad! {} On Standby!

- Flood Spam Division -

Commanding Officer-----: [Zycho-Dev!](http://t.me/Zycho_66)
Battalion Intelligence-----: [Team Zyntax](http://t.me/Zyntax_chat_zone)""".format(ALIVE_NAME),link_preview=False)
    except:
        pass