import asyncio
from typing import Awaitable


async def get_result(awaitable: Awaitable) -> str:
    try:
        result = await awaitable
    except Exception as e:
        print("oops!", e)
        return "no result :("
    else:
        return result

f = asyncio.Future()

loop = asyncio.get_event_loop()
loop.call_later(
    10,
    f.set_exception,
    ValueError("problem envountered")
) # <- when future be setted result, the job is done.
print(
    loop.run_until_complete(
        get_result(f)
    )
)