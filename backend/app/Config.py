import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")
    REDIS_URL = os.getenv("REDIS_URL")
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")

settings = Settings()
