import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1440))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1356469075))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Raghav2500/AnonXMusic-smaug",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/cameliaa_x_chat")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/cameliaa_x_chat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGYkZcAP_IU7NV7qI6X0C0_TPLAB8K9b0Kf-FHCcvQqS_xYj6BY3mrYQGgdG1LDnU5shb96n2mDf_bGFkRNrY9Gd34Z2SZ1L_srNG8na1SEPCRsZv73AM_FfI9YfqMN2up062qByfeYErtwQl0_fYT9Ko8gGsGMo8o76Zq6AOZpOpFxJKlmjelUJWD15bgf-FG0uHQLdbl3wnUBDTeDuzKzmI9UAK8lHwnidtJSMejszCKGdLls9G9KF-RnuTf5ZlXV6rgo6gfgjq8Dhjmov2fhnjqaVjFk4rFse55FcnGjASZawQCKbW4Csb9c2ufFwDvbFn13n0bW0rMaLtDz0SyCm0NyzAAAAAGD35M7AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
STATS_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/00cb4f8145b0c152e113d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
