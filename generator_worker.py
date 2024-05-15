import collections

def worker(f):
    tasks = collections.deque()
    value = None
    while True:
        batch = yield value
        value = None
        if batch is not None:
            tasks.extend(batch)
        else:
            if tasks:
                args = tasks.popleft()
                value = f(*args)

fun = lambda x: x*x

w = worker(fun)

print(w)
r = w.send(None)
print(f"{w=}")
print(f"{r=}")
p = w.send([(5,)])
print(f"{p=}")
k = next(w)
print(f"{k=}")
