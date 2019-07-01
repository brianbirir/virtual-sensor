# Virtual IoT Sensor and Gateway
A virtual sensor and gateway for testing MQTT clients and brokers. This application can be used to create one or more virtual sensors dynamically that are connected to a virtual gateway.

## System Architecture
![system architecture](/docs/virtual_sensor_architecture.png)

## Requirements

* [Paho MQTT Python client](http://www.eclipse.org/paho/clients/python/docs/)
* Python 3
* A server setup with an MQTT message broker e.g. [Mosquitto MQTT message broker](https://mosquitto.org/), EMQTT etc

## Message Broker server
Ensure that the message broker configurations are setup in a `.env` file. You can configure this file to add your message broker server details.


## Testing

### Local Development Environment
Install mosquitto broker and run `mosquitto_sub` to subscribe to a topic:

```bash
mosquitto_sub -h 127.0.0.1 -t 'topic/#' -p 1883 -v
```

Refer to `mosquitton_sub --help` for more details on options for this command.

Then run this python client from the root of the project folder to publish data to the specified topic. Ensure you run the application within a virtual environment running Python 3.6+:

```bash
python -m src.main
```

On the terminal output for `mosquitto_sub` you should see the following for example:

```bash
sensor/test {"sensor_id": "b14d5976-df7c-4d63-88cb-2f9d8c849d6f", "sensor_type": "humidity", "sensor_measurement_unit": "degrees_celsius", "sensor_measurement": 2}
```

## Docker Environment

Deploy the Docker containers first from the project root:

```bash
docker-compose -f docker/docker-compose.yml up --build
```

The above command will build the required images first and then the containers.

To check mosquitto logs when you publish a message to the broker:

```bash
docker exec -it mosquitto_service tail -f mosquitto/log/mosquitto.log
```

The sample output:

```bash
1561888331: Config loaded from /mosquitto/config/mosquitto.conf.
1561888331: Opening ipv4 listen socket on port 1883.
1561888331: Opening ipv6 listen socket on port 1883.
1561888657: mosquitto version 1.6.3 terminating
1561888657: Saving in-memory database to /mosquitto/data/mosquitto.db.
1561888661: mosquitto version 1.6.3 starting
1561888661: Config loaded from /mosquitto/config/mosquitto.conf.
1561888661: Opening ipv4 listen socket on port 1883.
1561888661: Opening ipv6 listen socket on port 1883.
1561888692: New connection from 172.22.0.1 on port 1883
```