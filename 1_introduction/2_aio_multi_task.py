import asyncio
import time


async def task(tag, delay):
    for i in range(6):
        await asyncio.sleep(delay)
        print(f"[{time.strftime('%X')}] Task:{tag}, step {i}")


async def main():
    asyncio.create_task(task("Task 1", 1))
    await asyncio.create_task(task("Task 2", 2))


async def main_blocked():
    await asyncio.create_task(task("Task 1", 1))
    await asyncio.create_task(task("Task 2", 2))

if __name__ == "__main__":
    print('Run async ver.')
    asyncio.run(main())

    print('Run sync ver.')
    asyncio.run(main_blocked())
