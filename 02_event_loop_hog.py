import asyncio
from pathlib import Path
import sys
import os
import re
import datetime


loop = asyncio.get_event_loop()
def print_now():
    print(datetime.datetime.now())

def trampoline(name: str = "") -> None:
    """
    do someting then register themselve back
    """
    print(name, end="")
    print_now()
    loop.call_later(0.5, trampoline, name)

def hog():
    sum = 0
    for i in range(10_000):
        for j in range(10_000):
            sum += j
    return sum

# They're scheduling the next step after each, maintain ordering.
loop.call_soon(trampoline,"First")
loop.call_soon(trampoline, "Second")
loop.call_soon(trampoline, "Third")
# hog function kicked in and clogged(阻塞) the event loop util it was done.
loop.call_later(15,hog)
loop.call_later(25, loop.stop)

loop.run_forever()