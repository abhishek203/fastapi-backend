from datetime import date
from pydantic import BaseModel


class Transaction(BaseModel):
    t_id:int
    current_date: date
    amount: float
    currency: str
    category: str
    person_id: int
    fip_name: str
    desc: str
