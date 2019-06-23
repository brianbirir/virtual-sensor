import os
from pathlib import Path
from dotenv import load_dotenv


class Config:
    """Loading of configurations from dot env file"""
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    BROKER_PORT = os.getenv('BROKER_PORT')
    BROKER_TOPIC = os.getenv('BROKER_TOPIC')
    BROKER_QOS = os.getenv('BROKER_QOS')
    BROKER_KEEP_ALIVE = os.getenv('BROKER_KEEP_ALIVE')
    BROKER_USERNAME = os.getenv('BROKER_USERNAME')
    BROKER_PASSWORD = os.getenv('BROKER_PASSWORD')
    BROKER_URL = os.getenv('BROKER_URL')
