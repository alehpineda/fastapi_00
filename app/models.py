from pydantic import BaseModel
from typing import Optional

class Pokemon(BaseModel):
    name: str
    iv_spd: int
    iv_hp: int
    iv_atk: int
    sex: Optional[str] = None
