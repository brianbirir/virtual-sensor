# Virtual IoT Sensor and Gateway
A virtual sensor and gateway for testing MQTT clients. This application can be used to create one or more virtual sensors dynamically that are connected to a virtual gateway.

## Requirements

* [Paho MQTT Python client](http://www.eclipse.org/paho/clients/python/docs/)
* Python 3
* A server setup with an MQTT message broker e.g. [Mosquitto MQTT message broker](https://mosquitto.org/), EMQTT etc

## Message Broker server
Ensure that the message broker configurations are setup in a `.env` file. You can configure this file to add your message broker server details.
