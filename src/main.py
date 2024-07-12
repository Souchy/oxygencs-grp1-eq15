import json
import time
import logging

import requests
from signalrcore.hub_connection_builder import HubConnectionBuilder
from sqlalchemy.orm import Session

from config import config
from alchemy import alch, crud
from models.Temperature import Temperature
from models.HVACAction import HVACAction


class App:

    db: Session

    def __init__(self):
        self._hub_connection = None
        self.TICKS = 10

        # To be configured by your team
        self.HOST = config["HOST_SENSORS"]
        self.TOKEN = config["TOKEN_HVAC"]
        self.T_MAX = config["T_MAX"]
        self.T_MIN = config["T_MIN"]
        self.DATABASE_URL = config["DB_HOST"]

    def __del__(self):
        if self._hub_connection != None:
            self._hub_connection.stop()

    def start(self):
        """Start Oxygen CS."""
        self.setup_sensor_hub()
        self._hub_connection.start()
        self.db = alch.SessionLocal()
        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def setup_sensor_hub(self):
        """Configure hub connection and subscribe to sensor data events."""
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.HOST}/SensorHub?token={self.TOKEN}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )
        self._hub_connection.on("ReceiveSensorData", self.on_sensor_data_received)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(
            lambda data: print(f"||| An exception was thrown closed: {data.error}")
        )

    def on_sensor_data_received(self, data):
        """Callback method to handle sensor data on reception."""
        try:
            print(data[0]["date"] + " --> " + data[0]["data"], flush=True)
            timestamp = data[0]["date"]
            temperature = float(data[0]["data"])
            action = self.take_action(temperature)
            self.save_event_to_database(temperature, action, timestamp)
        except Exception as err:
            print(err)

    def take_action(self, temperature):
        """Take action to HVAC depending on current temperature."""
        action = None
        if float(temperature) >= float(self.T_MAX):
            action = "TurnOnAc"
        elif float(temperature) <= float(self.T_MIN):
            action = "TurnOnHeater"

        if action is not None:
            self.send_action_to_hvac(action)

        return action

    def send_action_to_hvac(self, action):
        """Send action query to the HVAC service."""
        r = requests.get(
            f"{self.HOST}/api/hvac/{self.TOKEN}/{action}/{self.TICKS}", timeout=10
        )
        details = json.loads(r.text)
        print(details, flush=True)

    def save_event_to_database(self, temperature, action, timestamp):
        """Save sensor data into database."""
        try:
            temperature = Temperature(temperature, timestamp)
            crud.create_temperature(self.db, temperature)
            if action is not None:
                hvac_action = HVACAction(action, timestamp)
                crud.create_hvac_action(self.db, hvac_action)

        except Exception as e:
            print(f"{type(e)} while saving temperature: {e}")


if __name__ == "__main__":
    app = App()
    app.start()
