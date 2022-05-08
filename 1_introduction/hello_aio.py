import asyncio
import time


async def main():
    print(time.strftime('%X'), " hello")
    await asyncio.sleep(1)
    print(time.strftime('%X'), " world")


if __name__ == "__main__":
    asyncio.run(main())
