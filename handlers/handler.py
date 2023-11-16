from datetime import date
import os
import sys
import asyncio

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db import database 

def get_current_budget_status(budgetID):

    person_list = asyncio.run(database.get_list_of_persons_in_budget(budgetID))
    category = asyncio.run(database.get_category_in_budget(budgetID))
    start_date = asyncio.run(database.get_start_time_in_budget(budgetID))
    amount = asyncio.run(database.get_amount_in_budget(budgetID))
    totals = 0
    for personID in person_list:
        a = asyncio.run(database.get_total_spending_for_particular_category(person_id=personID,category=category,start_date=start_date))
        if a is not float:
            continue
        totals = totals + a
        

    return 100-(100*totals/amount)
    

if __name__ == "__main__":
    get_current_budget_status(2)
    

