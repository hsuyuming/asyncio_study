# docker run -it --rm python:3.4.10 bash


import asyncio
import time

def regular_function():
    time.sleep(3)
    return 0

@asyncio.coroutine
def async_function(): # <- this one is generator
    yield from asyncio.sleep(3)
    return 0

regular_function()

loop = asyncio.get_event_loop()
loop.run_until_complete(async_function())

loop.run_until_complete(
    asyncio.gather(
        async_function(),
        async_function(),
        async_function()
    )
)
#[0, 0, 0]


# type(regular_function)
# <class 'function'>
# type(async_function)
# #<class 'function'>
# type(async_function())
# # <class 'generator'>