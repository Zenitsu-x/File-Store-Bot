import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 6834180565

MSG_EFFECT = 5046509860389126442

SHORT_URL = "linkshortify.com" # shortner url 
SHORT_API = "" 
SHORT_TUT = "https://t.me/How_To_Download_ATK/2"

# Bot Configuration
SESSION = "zenitsu"
TOKEN = "7976435464:AAHDowmhRUxcnlW5FrBKckQr0JG5BcF4Qfs"
API_ID = "20293219"
API_HASH = "4aef7d9e065d92f4a95736eaeb93d3ac"
WORKERS = 5

DB_URI = "mongodb+srv://nshubh345:1FmseyW0TKaWNMNo@cluster0.pgewb.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "zenitsu"

FSUBS = [[-1002172875461, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = -1002953776171 # just put channel id dont add
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002953776171": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1002953776171": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 10800
# Admin IDs
ADMINS = [6091537598, 7902398470]
# Bot Settings
DISABLE_BTN = True
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": "<b>›› Hᴇʏ!, {first} ~ <blockquote>Lᴏᴠᴇ Pᴏʀɴʜᴡᴀ? I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ Wɪᴛʜ Mᴀɴʏ Aᴅᴠᴀɴᴄᴇ Fᴇᴀᴛᴜʀᴇs.</blockquote></b>",
    "FSUB": "<b><blockquote>›› Hᴇʏ ×</blockquote>\n  Yᴏᴜʀ Fɪʟᴇ Is Rᴇᴀᴅʏ ‼️ Lᴏᴏᴋs Lɪᴋᴇ Yᴏᴜ Hᴀᴠᴇɴ'ᴛ Sᴜʙsᴄʀɪʙᴇᴅ Tᴏ Oᴜʀ Cʜᴀɴɴᴇʟs Yᴇᴛ, Sᴜʙsᴄʀɪʙᴇ Nᴏᴡ Tᴏ Gᴇᴛ Yᴏᴜʀ Fɪʟᴇs</b>",
    "ABOUT": "<b>›› Fᴏʀ Mᴏʀᴇ: @MakimaDude \n <blockquote expandable>›› Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ: <a href='https://t.me/ErrorCodez_Bots'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› Oᴡɴᴇʀ: @Zenitsu_Xy\n›› Lᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› Dᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› Dᴇᴠᴇʟᴏᴘᴇʀ: @SupexSonic</b></blockquote>",
    "REPLY": "<b>For More Join - @MakimaDude</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ Gᴇᴛ Aʟʟ Fɪʟᴇꜱ Iɴ A Sɪɴɢʟᴇ Lɪɴᴋ ‼️\n\n ⌯ Yᴏᴜʀ Lɪɴᴋ Iꜱ Rᴇᴀᴅʏ, Kɪɴᴅʟʏ Cʟɪᴄᴋ Oɴ Oᴘᴇɴ Lɪɴᴋ Bᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://telegra.ph/file/fee99f091e6352fb81df0-f76172e5916d37d5c6.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
