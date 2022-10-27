from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "11762703"))
API_HASH = getenv("API_HASH", "49e935e55b4cb535ed80324b62d1a381")
BOT_TOKEN = getenv("BOT_TOKEN","5659290649:AAEaINC8Pkqo1LnnKD5SHMYQId-7LR77IMQ")
BOT_NAME = getenv("BOT_NAME","ᴀᴍᴍᴜ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ")
BOT_USERNAME = getenv("BOT_USERNAME","serinota_music_bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQBmcEZUSDSMlstMbr0sRRctf_bqlrNskInFfPdNoBovB8uogztNdXUaF9u6lsp_Z4Lf570ymg5bbyQ8qSoI7f_87nH3IGOCHiCIDKTlzaXI88K5Bsrko8AXBTsImAB8FK48GrV2Vr7rydQBtcDz7R1QxYyUTb-nGLK3oyUrEG8nf-s69gIJ52G8maKiXFra6F_GyEFUR8LI1EPFzWFBwFmFwSDfkdgUg0P1v7WEu5Yt3uqKjsJcxulDvT6jKwsbtPkinPWDXU-WMAUa2r1x1LgIctRiQ2XQSbgKSEQxmeN9S_6lAJIj1KD3ZqYi0w4IEOmPz2ffrWbbOHNyC5uJa6P4AAAAAU6rzEEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5614849089").split()))
