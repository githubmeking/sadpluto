from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID",213))
API_HASH = getenv("API_HASH","321")

BOT_TOKEN = getenv("BOT_TOKEN", "sadsafsdfsdfdsfsd")
MONGO_URL = getenv("MONGO_URL", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID",6180151150))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/hurkanal")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hurkanal")
PLAYLIST = getenv("PLAYLIST", "https://t.me/hurkanal")

PLAYLIST_ID = int(getenv("PLAYLIST_ID", "-21212"))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
