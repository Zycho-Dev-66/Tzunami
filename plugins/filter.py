from posixpath import split
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
FILTERS = config.FILTERS
client = ub.client

@client.on(events.NewMessage)
async def filters(event):
    if FILTERS == "True":
        try:
            chat = await event.get_chat()
            lst = event.message.message
            words = lst.split()
            for word in words:
                if (word == "SriLanka") or (word == "Srilanka") or (word == "srilanka"):
                    await client.send_message(chat,"""🇱🇰❤ **The Motherland of the legends.. Respect Mother SL** ❤🇱🇰\n
    __From Team Zyntax__""")
                elif (word == "Zycho") or (word == "zycho") or (word == "Zychodev") or (word == "zychodev"):
                    await client.send_message(chat,"""Are you looking for my master **Zycho-Dev**?\n

    💡 Zycho Developer 💡
    🔮 Team Zyntax OFC 🔮\n
    ⚠ Beware of the psychomaniac nature ⚠\n
    🇱🇰__Owner @ Team Zyntax__ 🇱🇰""")
                elif (word == "Zyntax") or (word == "zyntax"):
                    await client.send_message(chat,"""❤** Home of the LEGENDS**? ❤\n

    💡 Beyond your imagination 💡
    🔮 Team Zyntax OFC 🔮\n
    ⚠ Beware of the psychomaniac nature ⚠\n

    🇱🇰 __Zyntax Nation__ 🇱🇰""")
                elif (word == "Bts") or (word == "bts") or (word == "BTS") or (word == "Army") or (word == "army"):
                    await client.send_message(chat,"""😂** BTS**? 😂\n

    if (BTS == gay):
    army = ultra gay pro max

    💡 #FACTS 💡
    ⚠ Beware of the homosexual behaviour ⚠\n

    🇱🇰 __Zyntax Nation__ 🇱🇰""")

        except AttributeError:
            pass