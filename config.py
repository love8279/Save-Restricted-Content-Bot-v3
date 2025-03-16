# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "20417561")
API_HASH = os.getenv("API_HASH", "c01124688b006ef00fa6ac926d6cb3e9")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_DB", "g17hr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "6938716674").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", None)) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", None)) # optional with -100
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
