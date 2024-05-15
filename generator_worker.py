import collections

def gen():
    q = collections.deque()
    while True:

    received = yield "foo"
    print(received)


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
a = gen()
print(a)
print(type(a))
a.send(None)
a.send('get this done')
