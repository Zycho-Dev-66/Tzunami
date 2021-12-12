# requirements

from telethon import events
from time import sleep
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
cmdraid = COMMAND_HANDLER+'rraid'

@client.on(events.NewMessage(outgoing=True,pattern=r''+ cmdraid))
async def raid(event):
    try:
        chat = await event.get_chat()
        replied = await event.get_reply_message()
        userrep = replied.sender.username
        try:
            cmdlen = len(event.message.message)
            count = int(event.message.message[6:cmdlen])
            await client.edit_message(event.message,"""**Tzunami_UB**\nRaid Processing...\n\nRaid Count : {}""".format(count))
            sleep(1)
            for i in range(0,count):
                await client.send_message(chat,"""@{} Hey!✊🏻 You wanna see what the hell is like ya? 😈 Come on then challenge me you MFSOB! LOL!😂""".format(userrep))
                i = i + 1
            await client.edit_message(event.message,"""**Tzunami_UB**\nRaided the user\n __{}__\n{} times..""".format(userrep,count))

        except:
            await client.edit_message(event.message,"""**Tzunami_UB**\nReply to a user""")
    except AttributeError:
        pass