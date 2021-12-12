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
cmd = COMMAND_HANDLER+'help'

# help msg

@events.register(events.NewMessage(outgoing=True,pattern=r''+cmd))
async def help(event):
    chat = await event.get_chat()
    user = await client.get_me()
    await client.edit_message(event.message,"""**⚡ Tzunami Spambot Help Menu ⚡**\n

**🔮 Spambot Ultra Pro Max 🔮**\n

Master---: [{}](https://t.me/{})
Up since-: {}
Status---: `Standby`

⚠ **BE WARNED** ⚠\n

Dev-------: [@Zycho_66](https://t.me/Zycho_66)
Team-----: [Team Zyntax](https://t.me/Zyntax_chat_zone)

**Module-----** : ALIVE
**Cmd---------** : alive
**Description** : Check alive status of the bot\n\n

**Module-----** : HELP
**Cmd---------** : help
**Description** : Display the help menu\n\n

**Module-----** : FILTERS
**Cmd---------** : -
**Description** : Auto filters (Default)\n\n

**Module-----** : PING
**Cmd---------** : ping
**Description** : Check the ping\n\n

**Module-----** : PING
**Cmd---------** : alert
**Description** : Sudo user info - attention cmd\n\n

**Module-----** : SPAM
**Cmd---------** : spam
**Example**-----: .spam 10
**Description** : Spam the replied message\n\n

**Module-----** : SPAM
**Cmd---------** : mspam
**Example**-----: .mspam 10
**Description** : Spam the replied media(Img/GIF/Video/Sticker)\n\n

**Module-----** : VIRUS
**Cmd---------** : virus
**Example**-----: .virus 10
**Description** : Spam the chat with lag viruses\n\n

**Module-----** : REPLYRAID
**Cmd---------** : rraid
**Example**-----: .rraid 10
**Description** : Raid the replied user with mentioned messages\n\n

**Meanwhile Zycho : අපි තමයි හොදටම කළේ**‍\n""".format(ALIVE_NAME,user.username,up_time),link_preview=False)
