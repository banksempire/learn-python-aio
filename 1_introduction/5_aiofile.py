import asyncio
from typing import Any


class AsyncFuncWapper:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args: Any) -> Any:
        return asyncio.get_running_loop().run_in_executor(
            None,
            self._func,
            *args
        )


class AIOWapper:
    def __init__(self, obj) -> None:
        self._obj = obj

    def __getattribute__(self, __name: str) -> Any:
        # You should always use super().__getattribute__
        # to access attribute of self

        return AsyncFuncWapper(
            super().__getattribute__(
                "_obj"
            ).__getattribute__(__name)
        )

    # def __getattr__(self, __name: str) -> Any:
    #     # This can also do the job
    #     return AsyncFuncWapper(
    #         self._obj.__getattribute__(__name)
    #     )


async def aopen(*args):
    return AIOWapper(
        await asyncio.get_running_loop().run_in_executor(
            None, open, *args
        )
    )


async def main():
    file = await aopen('test.txt', 'w+')

    # file.write('abc')
    await file.write('abc')
    # await file.close()

if __name__ == "__main__":
    asyncio.run(main())
