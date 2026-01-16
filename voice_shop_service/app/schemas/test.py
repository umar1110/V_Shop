
from pydantic import BaseModel

class TestItem(BaseModel):
    name: str
    value: int
