import json
import re
from uuid import getnode as get_mac_address
from .helpers.fixtures import Fixture


class Sensor:
    def __init__(self):
        pass

    @staticmethod
    def get_device_id():
        """Generate hardware address of device
        
        Returns:
            str : hardware address of device
        """
        mac_address = ':'.join(
                    ("%012X" % get_mac_address())[i:i+2] for i in range(0, 12, 2))
        return mac_address

    @staticmethod
    def get_payload():
        """Construct sensor payload
        """
        seed = Fixture()
        sensor_attributes = {}
        sensor_data = {
            'RTC': seed.rtc(),
            'LS': seed.leak_sensor(),
            'FS': seed.fire_sensor(),
            'SS': seed.smoke_sensor(),
            'FL': seed.waterflow_sensor()
        }

        # sensor object with payload object and device id
        sensor_attributes['device_id'] = re.sub('[!@#$:]', '', Sensor.get_device_id())
        sensor_attributes['device_data'] = sensor_data
        return json.dumps(sensor_attributes)
