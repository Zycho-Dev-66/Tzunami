# Zyntax Nation
# Revenge Spambot

print("""[Tzunami]  Full throttle.. Engines starting up...\n""")
print(f"""
 _____                                _
|_   _|____   _ _ __   __ _ _ __ ___ (_)
  | ||_  / | | | '_ \ / _` | '_ ` _ \| |
  | | / /| |_| | | | | (_| | | | | | | |
  |_|/___|\__,_|_| |_|\__,_|_| |_| |_|_|
\n\n""")

from logging import CRITICAL
from time import sleep
from plugins import alive,spam,virus,ping,filter,replyraid,help
from telethon.tl.functions.channels import JoinChannelRequest

print('\n')
print("""[Tzunami]  Importing The Plugins...\n""")
print("""[Tzunami]  Modules : 06""")
print("""[Tzunami]  Plugins : 12\n""")

import base.client

client = base.client.client

#----------------- CMD ALIVE
with client as Tzunami:
    Tzunami.add_event_handler(alive.alive)

#----------------- CMD SPAM
with client as Tzunami:
    Tzunami.add_event_handler(spam.spam)

#----------------- CMD MEDIASPAM
with client as Tzunami:
    Tzunami.add_event_handler(spam.mediaspam)

#----------------- CMD VIRUS
with client as Tzunami:
    Tzunami.add_event_handler(virus.virus)

#----------------- CMD PING
with client as Tzunami:
    Tzunami.add_event_handler(ping.ping)

#----------------- CMD ALERT
with client as Tzunami:
    Tzunami.add_event_handler(ping.alert)

#----------------- CMD ATTENTION
with client as Tzunami:
    Tzunami.add_event_handler(ping.attention)

#----------------- CMD FILTERS
with client as Tzunami:
    Tzunami.add_event_handler(filter.filters)

#----------------- CMD REPLYRAID
with client as Tzunami:
    Tzunami.add_event_handler(replyraid.raid)

#----------------- CMD HELP
with client as Tzunami:
    Tzunami.add_event_handler(help.help)

print("""[Tzunami]  Imported The Plugins...\n""")
print("""[Tzunami]  Preparing to take off...\n""")
sleep(1)
client.start()
print("""[Tzunami]  Successfully started the spambot...\n""")

try:
    helpgroup = client.get_entity('t.me/Zyntax_chat_zone')
    helpchannel = client.get_entity('t.me/Zyntax_Nation')
    client(JoinChannelRequest(helpgroup))
    client(JoinChannelRequest(helpchannel))
    print("""[Tzunami]  Check our Help Group for more support...\n""")
except Exception as e:
    print(e)

client.run_until_disconnected()