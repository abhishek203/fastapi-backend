from fastapi import FastAPI
from models.budget import Budget
from db.database import *
from handlers.handler import BudgetHandler

app = FastAPI()


@app.post("/budget/create/")
def create_budget(budget: Budget):
    add_budget_to_db(budget)


@app.get("/budget/status/{budgetID}")
def get_current_status(budgetID: int):
    budget_handle = BudgetHandler(budgetID)
    return budget_handle.get_current_budget_status()


@app.post("/budget/update/{budgetID}")
def update_budget_amount(budgetID: int,new_amout:float):
    update_budget_amount_in_db(budgetID,new_amout)
