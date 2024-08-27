import asyncio

async def task1():
    await asyncio.sleep(1)
    return 1

async def task2():
    await asyncio.sleep(2)
    raise ValueError("Task 2 failed")

async def task3():
    await asyncio.sleep(3)
    return 3

async def main():
    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2()),
        asyncio.create_task(task3())
    ]

    done, pending = await asyncio.wait(tasks)

    for task in done:
        try:
            result = task.result()
            return result
        except Exception as e:
            pass


    # Cancel pending tasks if needed
    for task in pending:
        task.cancel()

result = asyncio.run(main())
print(result)
