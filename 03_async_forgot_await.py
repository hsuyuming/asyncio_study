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
    waiter = asyncio.wait_for(kp, 3)
    try:
        waiter # oops, forgot `await`!
    except asyncio.TimeoutError:
         print("oops, time's up")



asyncio.run(async_main())

"""
PYTHONASYNCIODEBUG=1 PYTHONTRACEMALLOC=1 python <python_file>
/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/events.py:80: RuntimeWarning: coroutine 'wait_for' was never awaited
  self._context.run(self._callback, *self._args)
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/events.py:80: RuntimeWarning: coroutine 'keep_printing' was never awaited
  self._context.run(self._callback, *self._args)
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
"""