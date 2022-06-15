import datetime
import asyncio

def print_now():
    print(datetime.datetime.now())


async def print3times() -> None:
  for _ in range(3):
    print_now()
    await asyncio.sleep(0.1)

coro1 = print3times()
coro2 = print3times()
print(type(print3times)) #<class 'function'>
print(type(coro1)) # <class 'coroutine'>
print(type(coro2)) # <class 'coroutine'>

# asyncio.run(print3times)
# """
# Traceback (most recent call last):
#   File "/asyncio_example/03_async_coroutines.py", line 19, in <module>
#     asyncio.run(print3times)
#   File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/runners.py", line 37, in run
#     raise ValueError("a coroutine was expected, got {!r}".format(main))
# ValueError: a coroutine was expected, got <function print3times at 0x102749ee0>
# sys:1: RuntimeWarning: coroutine 'print3times' was never awaited
# """

asyncio.run(coro1)
asyncio.run(coro2)
asyncio.run(coro1)
"""
Traceback (most recent call last):
  File "/Users/abehsu/Documents/SMTS_GDML_TEAM/asyncio_example/03_async_coroutines.py", line 32, in <module>
    asyncio.run(coro1)
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
RuntimeError: cannot reuse already awaited coroutine
"""