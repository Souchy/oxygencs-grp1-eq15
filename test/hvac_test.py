import unittest
from src.main import App
from src.alchemy import alch


class HVACTest(unittest.TestCase):

  # Set up
  def setUp(self):
    self.app = App()
    self.app.setup_sensor_hub()
    self.app.db = alch.SessionLocal()    

  def test_take_action_heater(self):
    action = self.app.take_action(0)
    self.assertAlmostEquals(action, "TurnOnHeater")

  def test_take_action_ac(self):
    action = self.app.take_action(50)
    self.assertAlmostEquals(action, "TurnOnAc")

  def tearDown(self):
    pass

if __name__ == "__main__":
    unittest.main()
