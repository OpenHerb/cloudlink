# -*- coding: utf-8 -*-
import time
import os
import pyrebase
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
    while True:
        temp = float(input("T: "))
        humidity = float(input("H: "))
        lux = float(input("L: "))
        firebase.publish(
            {
                "T": temp,
                "H": humidity,
                "L": lux,
                "I": datetime.isoformat(datetime.utcnow())
            }
        )
