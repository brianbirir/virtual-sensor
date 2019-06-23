"""Entry point of application
"""
from .publisher import Publisher
from .sensor import Sensor
from .config import Config

# load configurations
broker_url = Config.BROKER_URL
port = Config.BROKER_PORT
keep_alive = Config.BROKER_KEEP_ALIVE
username = Config.BROKER_USERNAME
password = Config.BROKER_PASSWORD

pub = Publisher(topic=Config.BROKER_TOPIC,
                qos=Config.BROKER_QOS,
                broker_username=Config.BROKER_USERNAME,
                broker_password=Config.BROKER_PASSWORD,
                broker_port=Config.BROKER_PORT,
                broker_keepalive=Config.BROKER_KEEP_ALIVE,
                broker_address=Config.BROKER_URL)

# publish to MQTT broker
pub.publish(message_payload=Sensor.get_payload())
