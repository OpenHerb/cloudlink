# -*- coding: utf-8 -*-
import time
import os
import serial
from datetime import datetime
from cloudlink.rtd.rtd import RTDLink
import random


if __name__ == "__main__":
    
    firebase = RTDLink(
        os.environ['API_KEY'],
        os.environ['AUTH_DOMAIN'],
        os.environ['DB_URL'],
        os.environ['BUCKET']
    )

    # telemetry reporting loop
    if os.environ['CL_DEBUG'] != "true":
        try:
            serial_connection = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=9600,
                timeout=30.0
            )
        except (serial.SerialException, FileNotFoundError) as exc:
            print("Serial connection failed")
            exit(1)

        while True:
            try:
                line = serial_connection.readline()
            except serial.SerialException as exc:
                print("Failed to read sensorframe")
            else:
                humidity = 0.0
                lux = 0.0
                cpu_temp = 0.0
                temp = round(float(cpu_temp)/1000, 2)
                sensorframe = line.decode()
                print("Sensorframe: {}".format(sensorframe))
                for value in sensorframe.split('|'):
                    if value.split('&')[0] == 'SM':
                        humidity = int(value.split('&')[1])
                    elif value.split('&')[0] == 'LX':
                        lux = int(value.split('&')[1])
                firebase.publish(
                    {
                        "T": temp,
                        "H": humidity,
                        "L": lux,
                        "I": datetime.isoformat(datetime.utcnow())
                    }
                )
    else:
        # debug mode mocking serial sensorframe
        while True:
            time.sleep(10)
            sh = random.randint(0,100)
            rh = random.randint(0,100)
            lux = random.randint(0,10000)
            pa = random.randint(90,110)
            temp = random.randint(15,35)
            payload = {
                "TP": temp,
                "RH": rh,
                "PA": pa,
                "LX": lux,
                "SM": sh,
                "I": datetime.isoformat(datetime.utcnow())
            }
            firebase.publish(payload)
            print("Payload: {}".format(payload))