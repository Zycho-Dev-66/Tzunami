# requirements

from telethon import events
from time import sleep
import os
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

# cmds
cmdspam = COMMAND_HANDLER+'spam'
cmdmspam = COMMAND_HANDLER+'mspam'

@events.register(events.NewMessage(outgoing=True,pattern=r''+cmdspam))
async def spam(event):
    chat = await event.get_chat()
    replied = await event.get_reply_message()
    try:
        cmdlen = len(event.message.message)
        count = int(event.message.message[6:cmdlen])
        await client.edit_message(event.message,"""**Tzunami_UB**\nSpam Processing...\n\nSpam Count : {}""".format(count))
        sleep(1)
        for i in range(0,count):
            await client.send_message(chat,replied)
            i = i + 1
        await client.edit_message(event.message,"""**Tzunami_UB**\nSpammmed the message\n __{}__\n{} times..""".format(replied.message,count))

    except:
        await client.edit_message(event.message,"""**Tzunami_UB**\nReply to a text message..""")

@events.register(events.NewMessage(outgoing=True,pattern=r''+cmdmspam))
async def mediaspam(event):
    chat = await event.get_chat()
    replied = await event.get_reply_message()
    try:
        try:
            cmdlen = len(event.message.message)
            count = int(event.message.message[7:cmdlen])
            
            await client.edit_message(event.message,"""**Tzunami_UB**\nMedia Spam Processing...\n\nSpam Count : {}""".format(count))
            mediaspam = await replied.download_media()
            for i in range(0,count):
                await client.send_file(chat,mediaspam)
                i = i + 1
            await client.edit_message(event.message,"""**Tzunami_UB**\nSpammmed the media {} times..""".format(count))
            os.remove(mediaspam)

        except ValueError:
            await client.edit_message(event.message,"""**Tzunami_UB**\nSpam count not provided""")

    except AttributeError:
        await client.edit_message(event.message,"""**Tzunami_UB**\nReply to some media..\n Images,Videos,GIFs etc.""")
