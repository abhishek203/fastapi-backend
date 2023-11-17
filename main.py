from typing import Union
from datetime import date
from fastapi import FastAPI
from models.budget import Budget 
from models.people import People
from db.database import *
from handlers.handler import get_current_budget_status
from contextlib import asynccontextmanager


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await connect()
#     yield
#     await disconnect()

# app = FastAPI(lifespan=lifespan)
app = FastAPI()
@app.post("/budget/create/")
def create_budget(budget:Budget):
    add_budget_to_db(budget)

@app.get("/budget/status/{budgetID}")
def get_current_status(budgetID:int):
    # return get_current_budget_status(budgetID)
    return get_category_in_budget(budgetID)

@app.get("/budget/update/")
def update_budget_amount():
    pass

