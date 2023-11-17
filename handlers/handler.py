from datetime import date
import os
import sys
import asyncio

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db import database 

def get_current_budget_status(budgetID):

    person_list = tuple(asyncio.run(database.get_list_of_persons_in_budget(budgetID)))
    category = asyncio.run(database.get_category_in_budget(budgetID))
    start_date = asyncio.run(database.get_start_time_in_budget(budgetID))
    amount = asyncio.run(database.get_amount_in_budget(budgetID))
    budget_end_date = asyncio.run(database.get_end_time_in_budget(budgetID))
    end_date = min(budget_end_date,date.today())
    
    curr_date = start_date
    time_delta = (end_date - start_date)/10
    curr_date_list = []
    res = []
    while curr_date <= end_date:
        # print(start_date,curr_date)
        curr_date_list.append(curr_date)
        a = asyncio.run(database.get_total_spending_for_particular_category(person_list,category,start_date,curr_date))
        curr_date += time_delta
        
        res.append(round(100*(a/amount),2))
        
    return res
    

if __name__ == "__main__":
    print(get_current_budget_status(1))
    

