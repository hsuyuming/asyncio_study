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

# They're scheduling the next step after each, maintain ordering.
loop.call_soon(trampoline,"First")
loop.call_soon(trampoline, "Second")
loop.call_soon(trampoline, "Third")
loop.call_later(8, loop.stop)

loop.run_forever()

