import json
from uuid import uuid4
from paho.mqtt.client import Client
from .helpers import logger as app_logger
from .config import Config


class Gateway:
    cnf = Config()

    def __init__(self, message_payload=None):
        self._client = Client()
        self._message_payload = message_payload

    def publish(self):
        """publishes sensor data to MQTT broker on a given topic
        """
        full_message_payload = {
            'gateway_id': str(uuid4()),
            'gateway_data': str(self._message_payload)
        }
        try:
            self._client.publish(topic=self.cnf.BROKER_TOPIC,
                                 payload=json.dumps(full_message_payload),
                                 qos=self.cnf.BROKER_QOS)
            app_logger.info("Published: " +
                            str(full_message_payload) + 
                            " " +
                            "on topic: " + 
                            str(self.cnf.BROKER_TOPIC))
        except Exception as e:
            app_logger.error(str(e))
    
    # call back functions on connecting to broker
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        return_code = {
            0: "Connection successful",
            1: "Connection refused – incorrect protocol version",
            2: "Connection refused – invalid client identifier",
            3: "Connection refused – server unavailable",
            4: "Connection refused – bad username or password",
            5: "Connection refused – not authorised"
        }
        if rc == 0:
            app_logger.info("Broker connection was successful")
        else:
            app_logger.error(return_code.get(rc, 
                             "Unable to identify return code error!"))

    @staticmethod
    def on_message(client, userdata, msg):
        app_logger.info("Message received: {}".format(str(msg.payload)))

    @staticmethod
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            app_logger.error("Unexpected disconnection: \
                             result code {}".format(str(rc)))
        else:
            app_logger.info("Disconnection was successful")
    
    @staticmethod
    def on_log(client, userdata, level, buf):
        app_logger.info(buf)

    def connect_to_broker(self):
        """Connects to MQTT broker
        """
        self._client.on_connect = self.on_connect
        self._client.on_message = self.on_message
        self._client.on_log = self.on_log
        self._client.on_disconnect = self.on_disconnect

        if self.cnf.BROKER_USERNAME is not None or self.cnf.BROKER_PASSWORD is not None:
            try:
                self._client.username_pw_set(self.cnf.BROKER_USERNAME,
                                             self.cnf.BROKER_PASSWORD)
                app_logger.info("Set up username and password for broker.")
            except Exception as e:
                app_logger.error(str(e))
        else:
            app_logger.info("No username or password.")

        try:
            self._client.connect(self.cnf.BROKER_URL,
                                 self.cnf.BROKER_PORT,
                                 self.cnf.BROKER_KEEP_ALIVE)
            app_logger.info("Connected to broker.")
        except Exception as e:
            app_logger.error(str(e))

        self.publish()