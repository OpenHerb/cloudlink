import uuid
import time
import os
import sys
from paho.mqtt.client import Client

class MQTTClient:

    def __init__(self) -> None:
        self.uuid = str(uuid.uuid4())
        self.client = Client(self.uuid, True)
        self.telemetry_topic = os.environ['TELEMETRY_TOPIC']
        self.qos = 0
        self.client.connected_flag = False
        self.client.disconnect_flag = False
        self.client.bad_connection_flag=False

    def connect(self):
        """
        """
        hostname = os.environ['MQTT_BROKER']
        port = int(os.environ['PORT'])
        try:
            self.client.connect(hostname, port=port, keepalive=60)
        except ConnectionError as exc:
            print("Connection exception occurred while trying to connect to MQTT broker: {}".format(exc))
            sys.exit(1)
        while not self.client.connected_flag:
            time.sleep(1)
            print("Waiting for mqtt broker ...")
    
    def on_connect(self, client:Client, userdata, flags:dict, response:int):
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
            client.connected_flag=True
        else:
            print("on_connect received a bad response code:",response)
        
    def on_disconnect(self, client:Client, userdata, response:int):
        """
        Response Codes:
        0: Disconnect callback execution successful
        ~: Unexpected disconnection occurred
        """
        if response != 0:
            print("Unexpected disconnection from MQTT broker")
        else:
            print("Successfully disconnected from MQTT broker")
        client.connected_flag=False
    
    def telemetry(self) -> None:
        while True:
            time.sleep(1)
            self.client.publish(self.telemetry_topic, payload='test', qos=self.qos, retain=True)
