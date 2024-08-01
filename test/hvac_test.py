import unittest
from src.main import App
from src.alchemy import alch
from src.config import config


class HVACTest(unittest.TestCase):

    # Set up
    def setUp(self):
        self.app = App()
        self.app.setup_sensor_hub()
        self.app.db = alch.SessionLocal()

    def test_take_action_heater(self):
        temp = int(config["T_MIN"]) - 1
        action = self.app.take_action(temp)
        self.assertEqual(action, "TurnOnHeater")

    def test_take_action_ac(self):
        temp = int(config["T_MAX"]) + 1
        action = self.app.take_action(temp)
        self.assertEqual(action, "TurnOnAc")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
