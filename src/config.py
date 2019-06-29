import os
from pathlib import Path
from dotenv import load_dotenv


class Config:
    """Loading of configurations from dot env file"""
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    BROKER_PORT = int(os.getenv('BROKER_PORT'))
    BROKER_TOPIC = str(os.getenv('BROKER_TOPIC'))
    BROKER_QOS = int(os.getenv('BROKER_QOS'))
    BROKER_KEEP_ALIVE = int(os.getenv('BROKER_KEEP_ALIVE'))
    BROKER_USERNAME = str(os.getenv('BROKER_USERNAME'))
    BROKER_PASSWORD = str(os.getenv('BROKER_PASSWORD'))
    BROKER_URL = str(os.getenv('BROKER_URL'))
    LOGGING_FILE = str(os.getenv('LOGGING_FILE'))
