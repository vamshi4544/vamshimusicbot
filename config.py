from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9940431"))
API_HASH = getenv("API_HASH", "be6474d8873f903e7d0b3890946240d6")
BOT_TOKEN = getenv("BOT_TOKEN","5685766625:AAGyvs7AlNUTmR10i_7Ns7oYQDo2S4M_6Jo")
BOT_NAME = getenv("BOT_NAME","jessicabot")
BOT_USERNAME = getenv("BOT_USERNAME","jessicaaabot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQA1aePKEfvUwE3c8gctt7sxNoraUyuSa3fTCEPJ2X9Fz-JLB4qDUBvMCqA0p1WNeWa6oD07aiLd3I7w90HQL9Yf9euEEgaLefITHxN8isJD1TiO4LMJaulhgGaRWeBLrwpYWtr8cSURHFuLL3f8XyP4EhFYPrriVJr4HMoc7axhtqdUCEGzyScho2R9QBnqxU-Z6j2ctHsJ9nBWmZ1f2IwVsltvMjH-dsuF7VREkDzyxqMGLGUt6UQV55OlleaHg50cvk8wiSmkjklGzaRnancJVrU7Lbhy2jWgcXYvdIBbCIgdKP9oEIdfVGYKBINvmmIeQZMaov5XP-uwVplwdmODAAAAAUvNkR8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5566730527").split()))
