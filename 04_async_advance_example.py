import asyncio


"""
dir(asyncio.Task)
['__await__', '__class__', '__class_getitem__', '__del__', 
'__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '_asyncio_future_blocking',
 '_callbacks', '_cancel_message', '_coro', '_exception', '_fut_waiter',
  '_log_destroy_pending', '_log_traceback', '_loop', 
  '_make_cancelled_error', '_must_cancel', '_repr_info', '_result', 
  '_source_traceback', '_state', 'add_done_callback', 'cancel', 
  'cancelled', 'done', 'exception', 'get_coro', 'get_loop', 
  'get_name', 'get_stack', 'print_stack', 'remove_done_callback', 
  'result', 'set_exception', 'set_name', 'set_result']
"""

def indent(count: int) -> str:
    return " "*(6 -(count*3))


async def example(count: int) -> str:
    print(indent(count), "Before the first await")
    await asyncio.sleep(0)
    print(indent(count), "After the first await")
    if count == 0:
        print(indent(count), "Returning result")
        return "result"
    for i in range(count):
        print(indent(count), "Before await inside loop iterarion", i)
        await asyncio.sleep(i)
        print(indent(count), "After await inside loop iterarion", i)
    print(indent(count), f"Before await on example({count -1})")
    return await example(count-1) # await chains / yield from chains

class TraceStep(asyncio.tasks._PyTask):

    def _Task__step(self, exc=None): # wrap around the __step, to create some logging 
        print(f"<step name={self.get_name()} done={self.done()}>")
        result = super()._Task__step(exc=exc)
        print(f"</step name={self.get_name()} done={self.done()}>")

loop = asyncio.get_event_loop()

loop.set_task_factory( 
    lambda loop, coro: TraceStep(coro, loop=loop)
)

loop.run_until_complete(example(1))
