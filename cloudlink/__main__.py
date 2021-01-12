# -*- coding: utf-8 -*-
import time
import os
import pyrebase
import serial
from datetime import datetime
from cloudlink.rtd.rtd import RTDLink


if __name__ == "__main__":
    
    firebase = RTDLink(
        os.environ['API_KEY'],
        os.environ['AUTH_DOMAIN'],
        os.environ['DB_URL'],
        os.environ['BUCKET']
    )

    # telemetry reporting loop
    try:
        serial_connection = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            timeout=5.0
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
            sensorframe = line.decode()
            print("Sensorframe: {}".format(sensorframe))
            with open( "/sys/class/thermal/thermal_zone0/temp" ) as tempFile:
                cpu_temp = tempFile.read()
                tempFile.close()
            temp = round(float(cpu_temp)/1000, 2)
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
        time.sleep(5)
