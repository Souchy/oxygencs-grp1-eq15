import unittest
from src.alchemy import crud, alch
from src.models.Temperature import Temperature
from src.models.HVACAction import HVACAction


class DatabaseTest(unittest.TestCase):

    # Set up
    def setUp(self):
        self.db = alch.SessionLocal()

    def test_create_temperature(self):
        temperature = Temperature(23.53, "2024-07-01T17:43:09.3873322+00:00")
        crud.create_temperature(self.db, temperature)

    def test_create_hvac_action(self):
        hvac_action = HVACAction("TurnOnAc", "2024-07-01T17:43:09.3873322+00:00")
        crud.create_hvac_action(self.db, hvac_action)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
