import datetime
import asyncio
from inspect import isawaitable

def print_now():
    print(datetime.datetime.now())


async def keep_printing(name: str ="") -> None:
    """
    async expression do two things:
    1. await expression will block from executing anything else util whatever we are awaiting on is done.
    2. await expression allows asyncio to do something else. While we're waiting for the sleep (or other) to finish
    """
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.50) # means at least how long we will wait



async def async_functoin() -> None:
  await keep_printing()

coroutine = async_functoin()

print(type(async_functoin)) #<class 'function'>
print(type(coroutine)) # <class 'coroutine'>
print(isawaitable(async_functoin)) #False
print(isawaitable(coroutine)) #True