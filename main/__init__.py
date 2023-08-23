#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28543561
API_HASH = "16047d5f9c4a7907887ea5c8aa840618"
BOT_TOKEN = "6375149025:AAHgvLrR3yFVB96xdDUSaVhDuAWruFrWzqc"
SESSION = "AQGblaIAaU0p4Hlii5IT3R3lfXZ7HWLc7_crBrL5cQ6NkLWttLxqmiB8XXn8McuwOd8EIVUmuyb8Qh9L8OxOoIwwWwxbMwXKTi0W6I_nmeeiHchVAngqQQcOLQ9W2NA5x33ZQhz8ApxfNoV3c3bYUAbLqwDQN_fm8-ejELhd9Dx0ZEdJrwuyiu5H_cXY-grXoUsUggqHewnjt1LzU5bP2mzZzmW6g1uZ1dEov6a0UVp-M3g-D-_pVHQalX8lOYFEqDBY6iwWaZbl7IUVlDB9ONz6Fj5vvvLkjKP2MIb_v380Hq-BgLBByr7KlhL-sOtP3trNfK-O_xT-fLUU_icoAt2UaC5JowAAAABxW-8CAA"
FORCESUB = "coursebygodofhell_bot"
AUTH = 1901850370

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
