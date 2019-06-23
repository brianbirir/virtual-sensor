"""This helper module logs messages of different severity levels
"""
import logging


logger = logging.getLogger('ruleblox_broker')
app_log_handler = logging.FileHandler('/tmp/iot_mqtt_subscriber.log')
app_log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
app_log_handler.setFormatter(app_log_formatter)
logger.addHandler(app_log_handler)


def info(message):
    logger.setLevel(logging.INFO)
    logger.info(message)


def error(message):
    logger.setLevel(logging.ERROR)
    logger.error(message)


def warning(message):
    logger.setLevel(logging.WARNING)
    logger.warning(message)
