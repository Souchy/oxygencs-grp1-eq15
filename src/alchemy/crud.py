from sqlalchemy.orm import Session
from alchemy import alchmodels
from models import (Temperature, HVACAction)


def create_temperature(db: Session, temperature: Temperature, commit=True):
  db_temperature = alchmodels.Temperature(**temperature.dict())
  db.add(db_temperature)
  if commit:
      db.commit()
      db.refresh(db_temperature)
  return db_temperature

def create_hvac_action(db: Session, hvac_action: HVACAction, commit=True):
  db_hvac_action = alchmodels.HVACAction(**hvac_action.dict())
  db.add(db_hvac_action)
  if commit:
      db.commit()
      db.refresh(db_hvac_action)
  return db_hvac_action


def test():
   print("works")