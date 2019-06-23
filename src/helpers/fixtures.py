import time
from random import randint


class Fixture:
	"""Seeding of sensor data with random integer values
	"""

	def __init__(self):
		pass

	@staticmethod
	def leak_sensor():
		return randint(0,1)

	@staticmethod
	def fire_sensor():
		return randint(0,1)

	@staticmethod
	def smoke_sensor():
		return randint(0,1)

	@staticmethod
	def waterflow_sensor():
		return randint(0,1)

	@staticmethod
	def rtc():
		return int(time.time())
