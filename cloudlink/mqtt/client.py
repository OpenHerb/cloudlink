# -*- coding: utf-8 -*-
"""
MQTT Client
===========
Modified: 2021-11

Dependencies
------------
```
import json
import logging
from typing import Any
from paho.mqtt.client import Client, MQTTMessage

from cloudlink.models.telemetry import Telemetry
```

Copyright © 2021 OpenHerb.
"""

import json
import logging
from typing import Any
from paho.mqtt.client import Client, MQTTMessage

from cloudlink.models.telemetry import Telemetry


class MQTTClient(Client):

    def __init__(self, client_id: str, host: str, port: int, telemetry_topic: str) -> None:
        super().__init__(client_id)
        self._logger = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.telemetry_topic = telemetry_topic
        self.qos = 0
        self._logger.info("Initialized %s", __class__.__name__)

    def start(self) -> None:
        """
        Authenticate and connect to the MQTT broker
        """
        self.username_pw_set('/:microservice', 'microservice')
        try:
            self.connect(self.host, port=self.port, keepalive=60)
        except ConnectionError as exc:
            self._logger.error(
                "Connection exception occurred while trying to connect to MQTT broker: %s", exc)
            raise exc
        self.loop_start()
        self._logger.info("Connected to MQTT broker %s:%s", self.host, self.port)

    def on_message(self, client: Client, userdata: Any, msg: MQTTMessage):
        self._logger.debug("Received: %s from client: %s with userdata: %s", msg, client, userdata)

    def on_connect(self, client: Client, userdata: Any, flags: dict, response: int) -> None:
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
            self._logger.info("%s on_connect callback response OK", client)
        elif response == 4:
            self._logger.error("%s authentication failure: %s", client, response)
            return
        else:
            self._logger.error("%s on_connect received a bad response code: %s", client, response)

    def on_disconnect(self, client: Client, userdata: Any, response: int):
        """
        Response Codes:
        0: Disconnect callback execution successful
        ~: Unexpected disconnection occurred
        """
        if response != 0:
            self._logger.error(
                "Unexpected disconnection from MQTT broker with response: %s", response)
        else:
            self._logger.info("Successfully disconnected from MQTT broker")

    def publish_telemetry(self, telemetry: Telemetry) -> None:
        """
        Publish telemetry object to MQTT broker

        :param telemetry: device telemetry
        :type telemetry: Telemetry
        """
        self.publish(self.telemetry_topic, payload=json.dumps(telemetry.serialize()),
                     qos=self.qos, retain=True)
        self._logger.info("Published to %s: %s ", self.telemetry_topic, "\n" +
                          json.dumps(telemetry.serialize(), indent=2))
