
def gen():
    counter = 0
    while counter < 10:
        yield counter
        counter +=1

g = gen()
type(g) # <class 'generator'>

g.gi_running # False

g.gi_frame # <frame object at 0x7f243f88adc8>

g.gi_frame.f_locals # {}

next(g) # 0

g.gi_frame.f_locals #{'counter': 0}

next(g)
next(g)
next(g)
next(g)
next(g)
next(g)

g.gi_frame.f_locals #{'counter': 6}


def outer():
    yield -1
    yield from gen()
    yield 10

for result in outer():
    print(result)
# -1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10