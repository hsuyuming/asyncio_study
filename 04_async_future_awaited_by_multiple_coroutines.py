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
loop.call_later(10, f.set_result, "final result")
print(
        loop.run_until_complete(
        asyncio.gather(
            get_result(f),
            get_result(f),
            get_result(f)
        )
    )
) # ['final result', 'final result', 'final result']
