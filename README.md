
### Evenloop

Callback1 -> Callback2 -> Callback3

- Event loop can be started and stopped many times over
- We avoid doing very long operations at any given moment
- We are doing something as fast as possible

### select system call
- select -> we provide list of file descriptors (e.g: regular file, network socker, unix socker...etc) 
- Multiplexing(多工/複用) pattern call reactor
- I/O CP (I/O Completion Port) used for Windows -> Allow a pool threads to block on it, waiting for new event, when an event arrives on thar port, it wakes up just one thread to handle it -> proactor
- unix_events.py(Depend by our operation system and situation): Kqueue / epoll / "/dev/poll" / poll / select
- You don't have to set an event loop manually in most cases except for one important special case. Python only creates a default event loop only in the main thread! If you're starting new threads (secondary thread) or worker threads, for those, if you'd like to use a separate thread specific event loop, you will have to set it manually!
- python defaults to the safe thing which is not to create an event loop for you on worker or secondary by default
- if you are on production env. you should be running uvloop (b ase on libuv)

### Debug
- you can set loop.set_debug(True) to display event_loop debug informatoin (base_events.py -> _run_once)
