from datetime import date
from pydantic import BaseModel


class People(BaseModel):
    id:int
    name: str