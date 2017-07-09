# Get MAC Address from host computer and use it as an ID
# Make use of Python UUID

from uuid import getnode as get_mac


def get_mac_address():
    mac = get_mac()

    mac_address = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

    return mac_address
