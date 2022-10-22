from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "15229796"))
API_HASH = getenv("API_HASH", "4e3363ea7214ebab7a03b9300bba722c")
BOT_TOKEN = getenv("BOT_TOKEN","55477430:AAEslnoE30dn2O3zx1d43fSfet")
BOT_NAME = getenv("BOT_NAME","𝐇𝐨𝐧𝐞𝐲 𝐌𝐮𝐬𝐢𝐜")
BOT_USERNAME = getenv("BOT_USERNAME","Honey_Music_Robot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "ByoAU20YIxjTeHh3pE2iywimpxGecH2GLTOi6dMp3LOrCTmcS5xm5eJM1ZHKMsg_70JFZTppAebd1q1phDbBUz-Y2ZH_K14bXrz_YKG8o28iaGZJEWpgy_l5p1cO5A8N7y0bfnRzGJ03fi9wqvoec00GTUqugoNhnxWgm1WrSeFmkCFZD69iVKUoCWZTAJFOw48pFTfNap8b_RdCgA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5342963115").split()))
