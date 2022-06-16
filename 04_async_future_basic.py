import asyncio

fut = asyncio.Future()
print(fut.done()) # False

print(fut.cancelled()) #False 

# fut.result()
# """
# Traceback (most recent call last):
#   File "/Users/abehsu/Documents/SMTS_GDML_TEAM/asyncio_example/04_async_future.py", line 8, in <module>
#     fut.result()
# asyncio.exceptions.InvalidStateError: Result is not set.
# """


fut.set_result("result is set!")

print(fut.done()) # True

print(fut.cancelled()) # False 

print(fut.result()) # result is set!