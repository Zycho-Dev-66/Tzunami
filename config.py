import os
from os import getenv
from dotenv import load_dotenv

dirlist = os.listdir()

for item in dirlist:
    try:
        filename,fileext = os.path.splitext(item)
        if (fileext == ".env") or (fileext == ".env"):
            load_dotenv(item)
    except:
        pass

try:
    API_ID = getenv('API_ID')
    API_HASH = getenv('API_HASH')
    SESSION = getenv('SESSION')
    Hndler = getenv('COMMAND_HANDLER','\\.')
    if (Hndler[1] == "\\"):
        COMMAND_HANDLER = Hndler[1:10]
    else:
        COMMAND_HANDLER = Hndler
    LOGGER_ID = getenv('LOGGER_ID')
    ALIVE_NAME = getenv('ALIVE_NAME')
    ALIVE_PIC = getenv('ALIVE_PIC')
    FILTERS = getenv('FILTERS')
except:
    pass
