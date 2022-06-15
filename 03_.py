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

# asyncio.run(
#     asyncio.wait_for(
#         keep_printing(),
#         10 # giving the timeout
#     )
# )

async def async_main() -> None:
    try:
        await asyncio.wait_for(
            keep_printing("Hey"),
            10
        )
    except asyncio.TimeoutError:
        print("oops, time's up")

asyncio.run(async_main())