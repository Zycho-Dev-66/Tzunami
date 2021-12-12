import telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print(f"""
 _____                                _
|_   _|____   _ _ __   __ _ _ __ ___ (_)
  | ||_  / | | | '_ \ / _` | '_ ` _ \| |
  | | / /| |_| | | | | (_| | | | | | | |
  |_|/___|\__,_|_| |_|\__,_|_| |_| |_|_|
\n\n""")

print("MAINTAINED BY THE TEAM ZYNTAX")
print("String Session Generator for Tzunami Spambot")
print("")
print("Official Session-Gen Module by Zycho-Dev\n")

input("""To continue..\n
You must enter the values API ID and the API HASH
extract these from my.telegram.org

Press any key to continue : """)

API_ID = input("""Please enter your API ID >>
: """)

API_HASH = input("""Please enter your API HASH >>
: """)

confirm = input("""Session will be generated using the following API credentials.
API ID   : {}
API HASH : {}

Please confirm the process..
[Y/N]    : """.format(API_ID,API_HASH))

if (confirm == "Y") or (confirm == "y"):
   print("""Process accepted and the Session-Gen will continue..
   
Please enter your phone number in the international format below (Ex:+9470123456)\n""")
   
   with TelegramClient(StringSession(), API_ID, API_HASH) as client:
      try:
         client.start()
         client.send_message('me',"""**⚡ Tzunami Spambot Session Generated! ⚡**\nGen by [Zycho-Dev](https://t.me/Zycho_66)\n\n{}\n\n
**⚠ Do not share this with anyone! ⚠**""".format(client.session.save()),link_preview=False)
         print("""Yo-Yo! Ur String Session has been generated and sent to you..

Plz check your telegram saved messages..""")

      except ValueError as error:
         print("""The Session-Gen process failed!
Error : {}

ERR_VALUE_ERR
Please check your API ID & HASH..\n""".format(error))
         print("")

else:
   print("""Process aborted by the user..

ERR_USER_ABORTED\n""")