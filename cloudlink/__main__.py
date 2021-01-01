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
        time.sleep(5)
        firebase.publish(
            {
                "T": 30.4,
                "H": 30.4,
                "L": 40,
                "I": datetime.isoformat(datetime.utcnow())
            }
        )
