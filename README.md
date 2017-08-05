# Virtual Sensor
A virtual sensor for testing that produces random temperature and humidity values and uses `MQTT` as the messaging protocol to send data.

## Requirements

* [Paho MQTT Python client](http://www.eclipse.org/paho/clients/python/docs/)
* [Python UUID for Python 2.7.*](https://docs.python.org/2/library/uuid.html) - generates UUID of the device
* A server setup with a message broker e.g. [Mosquitto MQTT message broker](https://mosquitto.org/)

## Message Broker server
Ensure that the message broker configurations are setup in the `config.json` file. You can configure this file to add your message broker server details.
