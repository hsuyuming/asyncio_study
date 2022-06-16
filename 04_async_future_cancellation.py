import asyncio
from typing import Awaitable


async def get_result(awaitable: Awaitable) -> str:
    try:
        result = await awaitable
    except Exception as e: # <- Pokemon exception handling: http://wiki.c2.com/?PokemonExceptionHandling 
        print("oops!", e)
        return "no result :("
    else:
        return result

f = asyncio.Future()

loop = asyncio.get_event_loop()
loop.call_later(
    10,
    f.cancel
) # <- when future be setted result, the job is done.
print(
    loop.run_until_complete(
        get_result(f)
    )
)
"""
Traceback (most recent call last):
  File "/asyncio_example/04_async_future_cancellation.py", line 7, in get_result
    result = await awaitable
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/asyncio_example/04_async_future_cancellation.py", line 22, in <module>
    loop.run_until_complete(
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
asyncio.exceptions.CancelledError <- CancelledError are now Base Exception 

"""