# Generate random gateway values

from random import randint
import time


def leak_sensor():
	return randint(0,1)

def fire_sensor():
	return randint(0,1)

def smoke_sensor():
	return randint(0,1)

def waterflow_sensor():
	return randint(0,1)

def rtc():
	return int(time.time())