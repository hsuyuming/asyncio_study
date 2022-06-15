import datetime
import asyncio

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



async def async_main() -> None:
    kp = keep_printing("Hey")
    print(type(kp)) #<class 'coroutine'>
    waiter = asyncio.wait_for(kp, 3)
    print(type(waiter)) #<class 'coroutine'>
    try:
        await waiter
    except asyncio.TimeoutError:
         print("oops, time's up")

asyncio.run(async_main())