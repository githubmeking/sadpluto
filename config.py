from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID",20213849))
API_HASH = getenv("API_HASH","e97df0eca2a9531c80202c1a7d3f5721")

BOT_TOKEN = getenv("BOT_TOKEN", "6591274198:AAFFsE0pTw3tUE9kq49QjUBarwLaQTdjurY")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sadbot19033:sadbotbey@cluster0.01dwa.mongodb.net/")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID",6180151150))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/hurkanal")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hurkanal")
PLAYLIST = getenv("PLAYLIST", "https://t.me/hurkanal")

PLAYLIST_ID = int(getenv("PLAYLIST_ID", ""))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
