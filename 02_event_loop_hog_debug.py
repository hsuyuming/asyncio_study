import asyncio
from pathlib import Path
import sys
import os
import re
import datetime


loop = asyncio.get_event_loop()
loop.set_debug(True)
"""
Second2022-06-15 00:08:49.415686
Third2022-06-15 00:08:49.415851
Executing <TimerHandle when=15.100627496 hog() at /asyncio_example/02_event_loop_hog_debug.py:22 created at /asyncio_example/02_event_loop_hog_debug.py:34> took 4.919 seconds
First2022-06-15 00:08:54.823994
Second2022-06-15 00:08:54.824120
"""
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