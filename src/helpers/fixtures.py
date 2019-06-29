from random import randint, choice
from uuid import uuid4


class Fixture:
	"""Seeding of sensor data with random integer values
	"""

	def __init__(self):
		pass

	@staticmethod
	def sensor_measurement():
		return randint(0, 10)

	@staticmethod
	def sensor_id():
		return uuid4()

	@staticmethod
	def measurement_unit():
		units_list = ['degrees_celsius', '%', 'ppm']
		return choice(units_list)

	@staticmethod
	def sensor_type():
		type_list = ['temperature', 'humidity', 'concentration']
		return choice(type_list)
