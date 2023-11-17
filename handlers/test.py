import asyncio

async def my_task(arg1, arg2):
    # Your function that needs to be executed asynchronously
    print(f"Processing arguments: {arg1}, {arg2}")
    await asyncio.sleep(2)
    print(f"Task with arguments {arg1}, {arg2} finished")

async def run_tasks_concurrently(args_list):
    # Create tasks for each function call with different arguments
    tasks = [asyncio.create_task(my_task(*args)) for args in args_list]

    # Run tasks concurrently
    await asyncio.gather(*tasks)

# List of argument tuples for the function calls
arguments = [(1, 'a'), (2, 'b'), (3, 'c')]

# Run the event loop with the main coroutine
if __name__ == "__main__":
    asyncio.run(run_tasks_concurrently(arguments))