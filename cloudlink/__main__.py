# -*- coding: utf-8 -*-
"""
OpenHerb CloudLink
==================
Modified: 2021-11

Copyright © 2021 OpenHerb.
"""

import os
import time
import logging

from cloudlink.mqtt.client import MQTTClient
from cloudlink.models.telemetry import Telemetry

_log = logging.getLogger(__name__)

# RMQ Event config
host = os.environ['RABBITMQ_ADDR'].split(':')[0]
port = int(os.environ['RABBITMQ_ADDR'].split(':')[1])
telemetry_topic = os.environ.get('TELEMETRY_TOPIC', "topic/telemetry")
client_id = os.environ.get('CLIENT_ID', default="")

_log.debug("OpenHerb Client")
_log.debug("==========================================")
_log.debug("Client ID: %s", client_id)
_log.debug("RabbitMQ Broker: %s:%s", host, port)
_log.debug("Telemetry Topic: %s", telemetry_topic)

mqtt_client = MQTTClient(
    client_id=client_id,
    host=host,
    port=port,
    telemetry_topic=telemetry_topic
)
mqtt_client.connect()

while True:
    time.sleep(5)
    telemetry = Telemetry()
    telemetry.mock()
    mqtt_client.publish_telemetry(telemetry)
