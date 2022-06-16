def gen():
    counter = 0
    while counter < 10:
        new_value = (yield counter) # <- yield can return value too
        if new_value is not None:
            counter = new_value
        else:
            counter += 1

g = gen()
g.gi_frame.f_locals
next(g)
next(g)

g.gi_frame.f_locals # {'new_value': None, 'counter': 1}

g.send(7) #7
g.gi_frame.f_locals # {'new_value': 7, 'counter': 7}

g.send(10)
"""
>>> g.send(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""
g.gi_running #False

