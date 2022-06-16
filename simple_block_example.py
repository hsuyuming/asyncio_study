import asyncio
import time
import datetime

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
        # time.sleep(0.5)
        await asyncio.sleep(0.50) # means at least how long we will wait


async def async_main():
    await asyncio.gather( # gather: if the outer Future is cancelled, all children (that have not completed yet) are also cancelled.
        keep_printing("First"),
        keep_printing("Second"),
        keep_printing("Third")
    )

asyncio.run(async_main())