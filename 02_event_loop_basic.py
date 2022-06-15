import asyncio
from pathlib import Path
import sys
import os
import re
import datetime

loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete(asyncio.sleep(5))

def print_now():
    print(datetime.datetime.now())

# Schedule event/thing to be called
loop.call_soon(print_now)
loop.call_soon(print_now)

loop.run_until_complete(asyncio.sleep(5))


