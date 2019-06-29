# Virtual IoT Sensor and Gateway
A virtual sensor and gateway for testing MQTT clients. This application can be used to create one or more virtual sensors dynamically that are connected to a virtual gateway.

## System Architecture
![system architecture](docs/virtual_sensor_architecture.png?raw=true "System Architecture" | width=200)

## Requirements

* [Paho MQTT Python client](http://www.eclipse.org/paho/clients/python/docs/)
* Python 3
* A server setup with an MQTT message broker e.g. [Mosquitto MQTT message broker](https://mosquitto.org/), EMQTT etc

## Message Broker server
Ensure that the message broker configurations are setup in a `.env` file. You can configure this file to add your message broker server details.


## Testing
Install mosquitto broker and run `mosquitto_sub` to subscribe to a topic:

```bash
mosquitto_sub -h 127.0.0.1 -t 'topic/#' -p 1883 -v
```

Refer to `mosquitton_sub --help` for more details on options for this command.

Then run this python client from the root of the project folder to publish data to the specified topic:

```bash
python -m src.main
```

On the terminal output for `mosquitto_sub` you should see the following for example:

```bash
sensor/test {"sensor_id": "b14d5976-df7c-4d63-88cb-2f9d8c849d6f", "sensor_type": "humidity", "sensor_measurement_unit": "degrees_celsius", "sensor_measurement": 2}
```