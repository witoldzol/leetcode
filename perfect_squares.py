import math

def wrapper(n: int):
    cache = [0] * (n + 1)
    def solve(n: int):
        if n == 0:
            return 0
        if n < 0:
            return float('inf')
        max_range = math.floor(n ** 0.5)
        ans = float('inf')
        for i in range(1, max_range + 1):
            reminder = n - (i*i)
            if cache[reminder]:
                s = cache[reminder]
            else:
                s = solve(reminder)
                cache[reminder] = s
            ans = min(ans, 1 + s) 
        return ans
    return solve(n)

def iterative(n: int):
    cache = [float('inf')] * (n + 1)
    cache[0] = 0
    mid = math.floor(n ** 0.5)
    for i in range(n+1):
        for j in range(1, mid + 1):
            reminder = i - j * j
            cache[i] = min(cache[i], 1 + cache[reminder])
    return cache[n]


assert 1 == wrapper(4)
assert 3 == wrapper(12)
assert 2 == wrapper(13)
assert 1 == iterative(4)
assert 3 == iterative(12)
assert 2 == iterative(13)
# assert 2 == solve(1300)

def w(n: int):
    results = [-1] * n
    results[0] = 0
    results[1] = 1
    def bob(n:int):
        # what is the base case ?
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n < 0:
            raise Exception('Negative number detected')
        # greedy way is to get the sq root and check if we have a perfect square
        sqr = n ** 0.5
        if sqr % 1 == 0:
            return 1
        for i in range(1, n + 1): # if we want to do 12, we go through each n, and calculate MIN number of combinations 
            # i=1, r = 1
            # i=2, r = 2
            # i=3, r= #!/usr/bin/env python3
            # i=4 r=1
            for j in range(1, math.floor(sqr)):

def test_w():
    assert 1 == w(4)
    assert 3 == w(12)
    assert 2 == w(13)
