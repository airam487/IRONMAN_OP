import requests
from pyrogram import Client as Bot

from Musical.config import API_HASH
from Musical.config import API_ID
from Musical.config import BG_IMAGE
from Musical.config import BOT_TOKEN
from Musical.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID=7877541,
    API_HASH=819c23b9999b144dc7b8411fabb0d075,
    bot_token=1770563880:AAGM7sC25LFZYuqdFxDWM-7HRYd-RBnPkO8,
    plugins=dict(root="Musical.modules"),
)

bot.start()
run()
