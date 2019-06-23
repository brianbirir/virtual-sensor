from paho.mqtt.client import Client
from .helpers import logger as app_logger


class Publisher:
    def __init__(self, topic, qos, 
                 broker_username, 
                 broker_password,
                 broker_port,
                 broker_keepalive,
                 broker_address):
        self._client = Client()
        self._topic = topic
        self._qos = int(qos)
        self._username = broker_username
        self._password = broker_password
        self._keepalive = int(broker_keepalive)
        self._port = int(broker_port)
        self._address = broker_address

    def publish(self, message_payload):
        """publishes sensor data to MQTT broker on a given topic
        
        Args:
            message_payload (object): sensor data as json object
        """
        self.connect_to_broker()
        try:
            self._client.publish(self._topic, 
                                 message_payload, 
                                 self._qos)
            app_logger.info("Published: " +
                            str(message_payload) + " " +
                            "on topic: " + 
                            str(self._topic))
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

        try:
            self._client.username_pw_set(self._username,
                                         self._password)
        except Exception as e:
            app_logger.error(str(e))

        try:
            self._client.connect(self._address,
                                 self._port,
                                 self._keepalive)
        except Exception as e:
            app_logger.error(str(e))
