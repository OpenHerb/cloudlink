# -*- coding: utf-8 -*-

import json
import logging
from paho.mqtt.client import Client

from cloudlink.models.telemetry import Telemetry


class MQTTClient:

    def __init__(self, client_id: str, host: str, port: int, telemetry_topic: str) -> None:
        self._logger = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.telemetry_topic = telemetry_topic
        self.client_id = client_id
        self.client = Client(self.client_id)
        self.qos = 0

    def connect(self):
        """
        """
        try:
            self.client.connect(self.host, port=self.port, keepalive=60)
        except ConnectionError as exc:
            self._logger.error(
                "Connection exception occurred while trying to connect to MQTT broker: %s", exc)
            raise exc

    def on_connect(self, client: Client, userdata, flags: dict, response: int):
        """
        Response Codes:
        0: Connection successful
        1: Connection refused - incorrect protocol version
        2: Connection refused - invalid client identifier
        3: Connection refused - server unavailable
        4: Connection refused - bad username or password
        5: Connection refused - not authorised
        """
        if response == 0:
            print("on_connect callback response OK")
        else:
            print("on_connect received a bad response code:", response)

    def on_disconnect(self, client: Client, userdata, response: int):
        """
        Response Codes:
        0: Disconnect callback execution successful
        ~: Unexpected disconnection occurred
        """
        if response != 0:
            print("Unexpected disconnection from MQTT broker")
        else:
            print("Successfully disconnected from MQTT broker")

    def publish_telemetry(self, telemetry: Telemetry) -> None:
        """
        Publish telemetry object to MQTT broker

        :param telemetry: device telemetry
        :type telemetry: Telemetry
        """
        self.client.publish(self.telemetry_topic, payload=telemetry.serialize(),
                            qos=self.qos, retain=True)
        self._logger.info("Published to %s: %s ", self.telemetry_topic, "\n" +
                          json.dumps(telemetry.serialize(), indent=2))
