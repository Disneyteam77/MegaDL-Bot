# (c) @doreamonfans1 
# A Part of MegaDL-Bot <https://github.com/disneyteam77/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 123))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 1473138600))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL_UNAME = os.environ.get("LOG_CHANNEL_UNAME", "")


class TEXT:
  ABOUT = """
๐ค **Name:** {bot_name}

๐ **Language:** [Python](https://www.python.org)

๐ **Library:** [Pyrogram](https://docs.pyrogram.org)

๐ก **Hosted On:** [Heroku](https://heroku.com)

๐งโ๐ป **Owner:** [Doreamonfans](https://t.me/doreamonfans1)

๐ฅ **Support Group:** [Disney Team Chat](https://t.me/disneyteamchat)

๐ข **Updates Channel:** [Disney Team](https://t.me/disneygrou)
"""

  HELP_USER = """
I'm **Disney TeamMega DL Bot** 
I Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Me Any Mega.nz Link & See The Magic. (Mega Folder Isn't Supported Yet) You Can Also Change Caption: Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To The File & The Text You Wrote Will Be Attached As Caption ๐! 

**Note That:** When Starting Download One Mega Link, Bot Can Be Unresponsive For Other Users. See **@{log_chnl}** To Check If Another Task Is Running or Not. If You See **Bot Become Busy Now !!** Message As The Last Message Of The Channel, Please Wait Until You See The **Bot Become Free Now !!** Message. I Can't Upload Files Large Than `2.0 GB` As Telegram Upload Limitation!

**Made With โค๏ธ In ๐ฎ๐ณ By [Doreamonfans](https://t.me/doreamonfans1)!**
Feel Free To Say Buys or Any feature adding๐
"""

  START_TEXT = """
๐๐ป **Hi** {user_mention},

I'm **Disney TeamMega DL Bot**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More ๐!

**Maintained By: [Doreamonfans](https://t.me/doreamonfans1)**โค๏ธ!
"""
