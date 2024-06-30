from datetime import datetime
from pydantic import BaseModel

class HVACAction(BaseModel):
  id: int = None
  action: str = None
  taken_at: datetime = None

  def __init__(self, action, taken_at):
    super().__init__()
    self.action = action
    self.taken_at = taken_at