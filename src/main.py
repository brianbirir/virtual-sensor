"""Entry point of application
"""

from src.sensor import Sensor
from src.helpers.fixtures import Fixture


if __name__ == "__main__":
    fixture_data = Fixture()

    # publish to MQTT broker
    sensor_unit = Sensor(measurement=fixture_data.sensor_measurement(),
                         sensor_type=fixture_data.sensor_type(),
                         measurement_unit=fixture_data.measurement_unit())
    sensor_unit.post_payload()
