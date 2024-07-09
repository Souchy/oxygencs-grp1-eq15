from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, Float, DateTime, String
from src.alchemy.alch import Base, engine


class Temperature(Base):
    __tablename__ = "temperatures"
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    temperature: Mapped[float] = Column(Float)
    recorded_at: Mapped[datetime] = Column(DateTime)


class HVACAction(Base):
    __tablename__ = "hvac_actions"
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    action: Mapped[str] = Column(String)
    taken_at: Mapped[datetime] = Column(DateTime)


# Drop tables
# if False:
#     Temperature.__table__.drop(bind=engine)
#     HVACAction.__table__.drop(bind=engine)
#     print("alchmodels drop")

# Create tables
Base.metadata.create_all(bind=engine)
print("alchmodels create")
