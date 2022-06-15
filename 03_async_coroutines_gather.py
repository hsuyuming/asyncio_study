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

async def async_main() -> None:
  """
  instead of using many await, we will just use one, we can put our coroutines inside a gather coroutines
  Remember: we are not executing in parallel but concurrently, all of this is happening in a single thread
  """
  await asyncio.gather(
    keep_printing("First"),
    keep_printing("Second"),
    keep_printing("Third")
  )

asyncio.run(async_main())