import asyncio
import time


async def task(tag, delay):
    for i in range(6):
        await asyncio.sleep(delay)
        print(f"[{time.strftime('%X')}] Task:{tag}, step {i}")


async def main():
    await asyncio.gather(
        asyncio.create_task(task("Task 1", 1)),
        asyncio.create_task(task("Task 2", 2))
    )

if __name__ == "__main__":
    asyncio.run(main())
