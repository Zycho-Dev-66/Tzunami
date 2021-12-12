# requirements

from telethon import events
from time import sleep
from datetime import datetime
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

# vars

uptime = datetime.now()
up_time = uptime.strftime("%d-%M-%Y | %H:%M:%S")
cmd = COMMAND_HANDLER+'alive'

# alive msg
@events.register(events.NewMessage(outgoing=True,pattern=r''+cmd))
async def alive(event):
    chat = await event.get_chat()
    user = await client.get_me()
    await client.delete_messages(chat, event.message)
    await client.send_file(chat,file=ALIVE_PIC,caption="""**⚡ Hi! Tzunami Spambot is alive! ⚡**\n

#Tzunami_ALIVE\n
**🔮 Spambot Ultra Pro Max 🔮**\n

Master---: [{}](https://t.me/{})
Up since-: {}
Status---: `Standby`

⚠ **BE WARNED** ⚠\n

Dev-------: [@Zycho_66](https://t.me/Zycho_66)
Team-----: [Team Zyntax](https://t.me/Zyntax_chat_zone)

**TZUNAMI SPAMBOT** at your command!

**Meanwhile Zycho : අපි තමයි හොදටම කළේ**‍\n""".format(ALIVE_NAME,user.username,up_time),link_preview=False)
