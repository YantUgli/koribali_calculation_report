import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY" , "dev-secret-key")
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")