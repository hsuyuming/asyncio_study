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
    asyncio.create_task( # <- tell asyncio that now there is going to be a coroutine that asyncio tracks, it will run our thing in the background, it will only run whenever we are awaiting on something
        algo(url), # pass coroutine
        name=url # good practice to help us debugging
    )
    todo.add(url)
    start = time.time()
    while len(todo):
        print(
            f"{len(todo)}: "
            + ", ".join(
                sorted(todo)
            )[-38:]
        )
        await asyncio.sleep(0.5)
    end = time.time()
    print(f"Took {int(end-start)} seconds")

todo = set()
async def crawl1(
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
            todo.add(line)
            await crawl1(prefix, line)
    todo.discard(url)

asyncio.run(progess(addr, crawl1))