
import databases
import asyncio
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models import budget

DATABASE_URL = "postgresql://budget:grove@localhost/budget_db"

async def add_budget_to_db(b):
    query = f'''
    Insert into budget(budget_id,total_amount,start_day,category,currency,list_of_people_id,current_consumption,end_day)
    Values
    ({b.budget_id},{b.total_amount},
    '{b.start_date}','{b.category}',
    '{b.currency}','{b.list_of_people_id}',
    {b.current_consumption},'{b.end_date}'
    );
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    await db.execute(query)

    await db.disconnect()

async def get_total_spending_for_particular_category(person_list,category,start_date,end_date):
    # print(start_date,end_date)
    query = f'''
    select 
        sum(amount)
    from
        transaction
    where
        person_id in {person_list}
    and
        category = '{category}'
    and
       tran_day > '{start_date}'
    and
       tran_day < '{end_date}'
    '''
    # print(query)
    db = databases.Database(DATABASE_URL)

    await db.connect()

    result = await db.fetch_one(query)
    # print(result[0])
    await db.disconnect()
    try:
        if result[0] == None:
            return 0
    except:
        print("NO data in Budget table")
    return result[0]
async def get_list_of_persons_in_budget(budgetID):
    query = f'''
    select
        list_of_people_id
    from 
        budget
    where 
        budget_id = {budgetID}
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    result = await db.fetch_one(query)

    await db.disconnect()
    try:
        return result[0]
    except:
        print("NO data in Budget table")

async def get_category_in_budget(budgetId):
    query = f'''
    select
        category
    from
        budget
    where
        budget_id = {budgetId}
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    result = await db.fetch_one(query)

    await db.disconnect()
    try:
        return result[0]
    except:
        print("NO data in Budget table")

async def get_start_time_in_budget(budgetID):
    query = f'''
    select
        start_day
    from
        budget
    where
        budget_id = {budgetID}
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    result = await db.fetch_one(query)
    await db.disconnect()
    
    try:
        return result[0]
        
    except:
        print("NO data in Budget table")
    
   

    return result[0]

async def get_end_time_in_budget(budgetID):
    query = f'''
    select
        end_day
    from
        budget
    where
        budget_id = {budgetID}
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    result = await db.fetch_one(query)
    await db.disconnect()
    
    try:
        return result[0]
        
    except:
        print("NO data in Budget table")
    
   

    return result[0]

async def get_amount_in_budget(budgetID):
    
    query = f'''
    select
        total_amount
    from
        budget
    where
        budget_id = {budgetID}
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    result = await db.fetch_one(query)

    await db.disconnect()
    try:
        return result[0]
    except:
        print("NO data in Budget table")

async def update_budget_amount_in_db(budgetID,new_amount):
    
    query  = f'''
        update budget
        set total_amount = {new_amount}
        where
        budget_id = {budgetID};        
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    await db.execute(query)

    await db.disconnect()

async def delete_budget_entry_from_db(budgetID):
    query = f'''
    delete 
        from budget
    where
        budget_id = {budgetID};
    '''
    db = databases.Database(DATABASE_URL)

    await db.connect()

    await db.fetch_one(query)

    await db.disconnect()

if __name__ == "__main__":
    b = budget.Budget(budget_id=3,total_amount=1000,category='ff',currency='INR',start_date='2023-11-17',end_date='2023-12-17',list_of_people_id='{1,2,3}',current_consumption=11)
    # b.budget_id = 1
    # b.category = 'food'
    # b.currency = 'INR'
    # b.start_date = '2023-11-17'
    # b.end_date = '2023-12-17'
    # b.list_of_people_id = (1,2,3)
    # b.total_amount = 1000
    asyncio.run(add_budget_to_db(b))
    print(asyncio.run(delete_budget_entry_from_db(23)))
    # asyncio.run(add_budget_to_db(b))
    # print((asyncio.run(get_start_time_in_budget(1))))
    # print((asyncio.run(get_amount_in_budget(1))))
    # print((asyncio.run(get_total_spending_for_particular_category(1,'food','2023-11-01'))))
    # print((asyncio.run(get_category_in_budget(1))))
    # print(asyncio.run(get_list_of_persons_in_budget(1)))
    # asyncio.run(get_amount_in_budget(0))