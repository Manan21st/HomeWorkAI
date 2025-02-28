from pydantic_settings import BaseSettings

from dotenv import load_dotenv
import os

# Load .env manually when running locally
if not os.getenv("API_KEY"):  
    load_dotenv()


class Settings(BaseSettings):
    API_KEY: str

    class Config:
        env_file = "../.env" 
        case_sensitive = True

settings = Settings()
