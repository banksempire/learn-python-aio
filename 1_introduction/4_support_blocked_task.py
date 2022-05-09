import asyncio
import time


async def task(tag, delay):
    for i in range(6):
        await asyncio.sleep(delay)
        print(f"[{time.strftime('%X')}] Async Task:{tag}, step {i}")


def blocked_task(tag, delay):
    for i in range(6):
        time.sleep(delay)
        print(f"[{time.strftime('%X')}] Blocked Task:{tag}, step {i}")


async def main():
    loop = asyncio.get_running_loop()
    await asyncio.gather(
        # Run in thread
        loop.run_in_executor(None, blocked_task, "Task 1", 1),
        # Run in corotine
        asyncio.create_task(task("Task 2", 2))
    )

if __name__ == "__main__":
    asyncio.run(main())
