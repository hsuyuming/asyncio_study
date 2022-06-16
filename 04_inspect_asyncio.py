import asyncio

asyncio.Task # <class '_asyncio.Task'>

import _asyncio

_asyncio.__file__ #_asyncio.__file__

asyncio.tasks._CTask # <class '_asyncio.Task'>

asyncio.tasks._PyTask # <class 'asyncio.tasks.Task'>

type(asyncio.sleep) # <class 'function'>

coro = asyncio.sleep(0)

type(coro) # <class 'coroutine'>

dir(coro) # https://github.com/python/cpython/blob/3.9/Objects/genobject.c#L936-L942, https://github.com/python/cpython/blob/3.9/Objects/genobject.c#L958-L962
"""
['__await__', '__class__', '__del__', '__delattr__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__name__', 
'__ne__', '__new__', '__qualname__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', 'close', 'cr_await', 'cr_code', 
'cr_frame', 'cr_origin', 'cr_running', 'send', 'throw']
"""