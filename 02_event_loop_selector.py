import asyncio
from pathlib import Path
import sys
import os
import re
import datetime
import selectors

selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

def print_now():
    print(datetime.datetime.now())

# Schedule event/thing to be called
loop.call_soon(print_now)
loop.call_soon(print_now)

loop.run_until_complete(asyncio.sleep(5))

