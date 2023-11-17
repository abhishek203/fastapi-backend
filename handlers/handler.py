from db import database
from datetime import date
import os
import sys
import asyncio

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class BudgetHandler:
    def __init__(self, budgetID) -> None:
        self.person_list = tuple(asyncio.run(
            database.get_list_of_persons_in_budget(budgetID)))
        self.category = asyncio.run(database.get_category_in_budget(budgetID))
        self.start_date = asyncio.run(
            database.get_start_time_in_budget(budgetID))
        self.amount = asyncio.run(database.get_amount_in_budget(budgetID))
        self.budget_end_date = asyncio.run(
            database.get_end_time_in_budget(budgetID))
        self.end_date = min(self.budget_end_date, date.today())

    async def call_db_function(self, curr_date):

        return await database.get_total_spending_for_particular_category(self.person_list, self.category, self.start_date, curr_date)

    async def run_concurrently(self, curr_date_list):

        tasks = [asyncio.create_task(self.call_db_function(args))
                 for args in curr_date_list]

        return await asyncio.gather(*tasks)

    def get_current_budget_status(self):
        curr_date = self.start_date
        time_delta = (self.end_date - self.start_date)/5
        curr_date_list = []

        while curr_date <= self.end_date:
            curr_date_list.append(curr_date)
            curr_date += time_delta

        return curr_date_list,asyncio.run(self.run_concurrently(curr_date_list))
    
if __name__ == "__main__":
    pass

    # asyncio.run(run_concurrently(curr_date_list))
    # a = asyncio.run(database.get_total_spending_for_particular_category(person_list,category,start_date,curr_date))

    # res.append(round(100*(a/amount),2))

    # print(get_current_budget_status(1))
