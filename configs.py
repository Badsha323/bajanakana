# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is a TeleGram Search Bot of @Aks_support01_bot And Some Other Bots Available On TeleGram.

π€ My Name: <a href='https://t.me/mdisk1_search_bot'> Mα΄Ιͺsα΄ Sα΄α΄Κα΄Κ Κα΄α΄ </a>

π Language : <a href='https://www.python.org'> Python V3</a>

π Library: <a href='https://docs.pyrogram.org'> Pyrogram </a>

π‘ Server: <a href='https://heroku.com'> Heroku </a>

π¨βπ» Modified By: <a href='https://t.me/Imdb_updates'>Imdb-updates</a>

π Youtube: <a href='https://youtube.com/c/TechnicalAks01'>Technical Aks</a>

π₯ Bots Support: <a href='https://t.me/Imdb_updates'>IMDBBOTS</a>

π’ Bots Updates: <a href='https://t.me/Imdb_updates'>IMDB-BOTS</a></b>
"""
    
    ABOUT_HELP_TEXT = """<b>π¨βπ» Developers : <a href='https://t.me/Aks_support01_bot'>Aks</a>

BotsΒ are simply Telegram accounts operated by software β not people β and they'll often have AI features. They can do anything β teach, play, search, broadcast, remind, connect, integrate with other services, or even pass commands to the Internet of Things.

π I will help you to find Best Telegram Bots.

π If you Get Any Error In Searching Please Report at **@Aks_support01_bot**.

π Our Project Channel: <a href='https://t.me/Imdb_updates'>Imdb-updates</a>.

π All Bots Based On Users and Developer Demands. 

π€ Join For All Available Bots On Telegram: @Imdb_updates.
"""
    
    HOME_TEXT = """
<b>π Hey !{}, This is Online Search Botlist Bot <a href='https://t.me/mdisk1_search_bot'>mdisk</a>.

<a> Modified By : @Imdb_updates</a>

       <a> Credits goes to Everyone Who Supported.</b>

<a> Made With β€ By @Aks_support01_bot </a>
"""


    START_MSG = """
<b>π Hey {}, πΌπ π½π°πΌπ΄ πΈπ  <a href='https://t.me/mdisk1_search_bot'>mdisksearchbot</a>.
<a> πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½.. ππ·π΄π½ ππ΄π΄ πΌπ πΏπΎππ΄ππ β₯οΈβ₯οΈπ₯ </a>
"""
    ADD_BOTS = """<b>Heya! {} Want Same Like This Then Contact The Support.</b>"""
