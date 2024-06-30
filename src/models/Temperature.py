from datetime import datetime
from pydantic import BaseModel

class Temperature(BaseModel):
  id: int = None
  temperature: float = None
  recorded_at: datetime = None

  def __init__(self, temperature, recorded_at):
    super().__init__()
    self.temperature = temperature
    self.recorded_at = recorded_at