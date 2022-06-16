### Learning outcome: Coroutines 
- Let's talk about our Future (a.k.a: promise, deferred)
- How asyncio implements Futures
- Coroutines like it's 2012
- The heart of the Task
- The implementation of coroutines in 2020
- Custom awaitables
- The most common pitfall


### What is the future?
- It's an object serving as a container for a result which we will get in the future
- When we initial Future, it will get current event_loop (__init__)
- When we execute `add_done_callback`, it will schedule the callback on the event loop
- tasks -> support for coroutines and the scheduler
- tasks -> __step use trampoline pattern to enable concurrent execution 

### Common pitfall
- forget the add await (use `PYTHONASYNCIODEBUG=1 PYTHONTRACEMALLOC=1 python <file>`)
- return value happens to not be awaited on

### Performance
- event loop itself is already some computation. (e.g: selector, proactor handle I/O events, some collections event loop keeps internally for the callbacks and so on). none of this is free, all of the computation we're doing here has a price
- why asyncio provides better performance in the end is because as soon as there is networking involved, the actual network latency between server and client is typically orders of magnitude higher than the computational cost of maintaining an event loop and splitting your coroutines into small steps, by that time, this case will more efficient.
- blocking calls should not happen within async 