def foo(*args, **kwargs):
    print(f"{args}")
    print(type(args))
    print(f"{kwargs}")
    print(type(kwargs))

a = [1,2,3,4]
kw = {"a": 1, "b": 2}

# foo(f=a, lol=kw, foo=111, bar="ldfkjfdl")


def bar(*fargs, **slargs):
    print(f"{fargs}")
    print(type(fargs))
    print(f"{slargs}")
    print(type(slargs))

# bar(f=a, lol=kw, foo=111, bar="ldfkjfdl")

def z(**b):
    print(b)
    print(type(b))
z(**kw)
