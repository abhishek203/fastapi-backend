from datetime import date
from pydantic import BaseModel


class Budget(BaseModel):
    budget_id:int
    total_amount:float
    start_date: date
    category: str
    currency: str
    list_of_people_id: str
    current_consumption: float
    end_date: date
