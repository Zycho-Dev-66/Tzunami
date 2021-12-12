# requirements

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient
from time import sleep
import config as config

API_ID = config.API_ID
API_HASH = config.API_HASH
SESSION = config.SESSION
COMMAND_HANDLER = config.COMMAND_HANDLER
LOGGER_ID = config.LOGGER_ID
ALIVE_NAME = config.ALIVE_NAME
ALIVE_PIC = config.ALIVE_PIC

# parse mode = markdown

# check login status
try:
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    print("""[Tzunami]  Successfully Logged in as Tzunami Spambot""",flush=True)
    client.start()

    # startup alert
    
    if LOGGER_ID != "":
        try:
            logger = client.get_entity(int(LOGGER_ID))
            client.send_file(logger,file='https://telegra.ph/file/050540d246273c5daaa94.jpg', caption="""**⚡ Tzunami SpamBot #Tzunami_UB ⚡**\n

    **⚠ ZYNTAX NATION ⚠**\n
    **🔮 Advanced Telethon Spambot 🔮**\n

    Type `.alive` for checking alive status
    Type `.help` for the help menu

    💡 **Developed by [@Zycho_66](https://t.me/Zycho_66)**\n
    💡 **Maintained by [Team Zyntax](https://t.me/Zyntax_chat_zone)**\n


    **⚠ YOU MAY USE #TZUNAMI ON YOUR OWN RESPONSIBILITY ⚠**""")
        except Exception as err:
            client.send_message('me',"""**Tzunami_UB #Tzunami_ERR**\nUnable to find the logger group :`{}`\n\n
    Error : `{}`\n
    **ERR_LOGGER_NOT_FOUND**""".format(LOGGER_ID,err))
            client.send_file('me',file='https://telegra.ph/file/050540d246273c5daaa94.jpg', caption="""**⚡ Tzunami SpamBot #Tzunami_UB ⚡**\n

    **⚠ ZYNTAX NATION ⚠**\n
    **🔮 Advanced Telethon Spambot 🔮**\n

    Type `.alive` for checking alive status
    Type `.help` for the help menu

    💡 **Developed by [@Zycho_66](https://t.me/Zycho_66)**\n
    💡 **Maintained by [Team Zyntax](https://t.me/Zyntax_chat_zone)**\n


    **⚠ YOU MAY USE #TZUNAMI ON YOUR OWN RESPONSIBILITY ⚠**""")

    else:
        client.send_file('me',file='https://telegra.ph/file/050540d246273c5daaa94.jpg', caption="""**⚡ Tzunami SpamBot #Tzunami_UB ⚡**\n

    **⚠ ZYNTAX NATION ⚠**\n
    **🔮 Advanced Telethon Spambot 🔮**\n

    Type `.alive` for checking alive status
    Type `.help` for the help menu

    💡 **Developed by [@Zycho_66](https://t.me/Zycho_66)**\n
    💡 **Maintained by [Team Zyntax](https://t.me/Zyntax_chat_zone)**\n


    **⚠ YOU MAY USE #TZUNAMI ON YOUR OWN RESPONSIBILITY ⚠**""")
except:
    print("""[Tzunami]  Login Error : Please check your login creds""",flush=True)
    exit()
