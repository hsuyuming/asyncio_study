from typing import Coroutine
import httpx
import asyncio
import time
from typing import Callable
 
addr = "https://langa.pl/crawl/"

async def progess( 
    url: str,
    algo: Callable[..., Coroutine] # return coroutine
) -> None: # reporting async function
    task = asyncio.create_task( # <- tell asyncio that now there is going to be a coroutine that asyncio tracks, it will run our thing in the background, it will only run whenever we are awaiting on something
        algo(url), # pass coroutine
        name=url # good practice to help us debugging
    )
    todo.add(task)
    start = time.time()
    while len(todo):
        done, _pending = await asyncio.wait( # this function will not raise exception
            todo, # <- take collection of tasks
            timeout=0.5
        )
        todo.difference_update(done)
        urls = ( t.get_name() for t in todo)
        print(
            f"{len(todo)}: " + ", ".join(
                sorted(urls)
            )[-75:]
        )
    end = time.time()
    print(f"Took {int(end-start)} seconds")

todo = set()
async def crawl2(
    prefix: str, url:str = ""
) -> None:
    url = url or prefix
    client = httpx.AsyncClient(verify=False)
    try:
        res = await client.get(url)
    finally:
        await client.aclose()
    for line in res.text.splitlines():
        if line.startswith(prefix):
            task = asyncio.create_task(
                crawl2(prefix, line),
                name=line
            )
            todo.add(task)

async def async_main() -> None:
    try:
        await progess(addr, crawl2)
    except asyncio.CancelledError: # <- Cancellations as exception only happen during await expressions
        for task in todo:
            task.cancel()
        done, pending = await asyncio.wait(todo, timeout=1.0)
        todo.difference_update(done)
        todo.difference_update(pending)
        if todo:
            print("warning: more tasks added while we were cancelling")

loop = asyncio.get_event_loop()
task = loop.create_task(async_main())
loop.call_later(5, task.cancel)
loop.run_until_complete(task)