import math
# n = 4
# for 1 - 4 we look at the all posible combos
# i = 1
# perfect square, return 1
# i = 2 , reminder 1, 1 + fun(1) => 2

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

