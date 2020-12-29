# -*- coding: utf-8 -*-

import os
import logging
from paho.mqtt.client import Client


class MQTT:

    def __init__(self) -> None:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(threadname)s %(name)s %(message)s"
        )
        self.telemetry_topic = os.environ['TELEMETRY_TOPIC']
        self.qos = 0
        self.client = Client()

    def start(self):
        """
        """
        self.client.connect('localhost', port=5000, keepalive=60, bind_address="")

    def publish(self, payload:dict):
        """
        """
        self.client.publish(self.telemetry_topic, payload=payload, qos=self.qos, retain=True)

if __name__ == "__main__":
    mqtt = MQTT()
    mqtt.start()
