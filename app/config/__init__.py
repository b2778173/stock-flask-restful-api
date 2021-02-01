from dotenv import load_dotenv
import os

load_dotenv()


class config:

    FINNHUB_BASE_URL = os.getenv("FINNHUB_BASE_URL")
    API_KEY = os.getenv("API_KEY")
    MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
