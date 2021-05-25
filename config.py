import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
URL = os.getenv("URL")
ID_ADMIN = int(os.getenv("ID_ADMIN"))
