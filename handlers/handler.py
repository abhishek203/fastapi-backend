from datetime import date, timedelta
import os
import sys
import asyncio
from multiprocessing import Process

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db import database

def get_current_budget_status(budgetID):

    person_list = asyncio.run(database.get_list_of_persons_in_budget(budgetID))
    category = asyncio.run(database.get_category_in_budget(budgetID))
    start_date = asyncio.run(database.get_start_time_in_budget(budgetID))
    budget_end_date = asyncio.run(database.get_end_time_in_budget(budgetID))
    amount = asyncio.run(database.get_amount_in_budget(budgetID))
    today_date = date.today()
    end_date = min(budget_end_date, today_date)
    asyncio.run(process(start_date,end_date,person_list,category))
    
async def process(start_date,end_date,person_list,category):
    curr_date = start_date
    time_delta = (end_date - start_date)/30
    curr_date_list = []

    args = [tuple(person_list),category,start_date]
    arg_list = []
    while curr_date <= end_date:
        temp_list = [tuple(person_list),category,start_date]
        curr_date += time_delta
        curr_date_list.append(curr_date)
        temp_list.append(curr_date)
        arg_list.append(temp_list)
    
    for arg in arg_list:
        print(*arg)
    # tasks = [asyncio.create_task(database.get_total_spending_for_particular_category(*arg_list[1]) )]
    # totals_list.append([curr_date, float(a/amount)])
    # print(type(tasks[0]))
    res = asyncio.gather(database.get_total_spending_for_particular_category(*arg_list[2]) )
    print(res)

    
if __name__ == "__main__":
    (get_current_budget_status(1))
