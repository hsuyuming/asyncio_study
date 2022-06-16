import asyncio
from typing import Awaitable

def callback(fut: asyncio.Future) -> None:
    print("called by", fut)

loop = asyncio.get_event_loop()
f = asyncio.Future()

f.add_done_callback(callback) # <- Add a callback to be run when the future becomes done
f.add_done_callback(lambda f : loop.stop())
f.set_result("yup") # <- nothing happen 
loop.run_forever() # <- suprising, callback run on the event loop and not directly on the future when result is set.
#<-called by <Future finished result='yup'>