# -*- coding: utf-8 -*-
import pyrebase

class RTDLink:

    def __init__(self,apikey:str,authd:str,url:str,bucket:str) -> None:

        config = {
            "apiKey": apikey,
            "authDomain": authd,
            "databaseURL": url,
            "storageBucket": bucket
        }
        firebase = pyrebase.initialize_app(config)
        # Get a reference to the database service
        self.db = firebase.database()
        
    def publish(self, payload:dict):
        # Pass the user's idToken to the push method
        response = self.db.push(payload)
        print(response)