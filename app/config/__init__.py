from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    FINNHUB_BASE_URL = os.getenv("FINNHUB_BASE_URL")
    API_KEY = os.getenv("API_KEY")


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")


class TestingConfig(Config):
    DEBUG = True
    MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")


class ProductionConfig(Config):
    DEBUG = True
    MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default' : DevelopmentConfig
}
