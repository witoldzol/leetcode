import math

def solve(n: int, cache = None):
    if not cache:
        cache = [0] * (n + 1)
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
            s = solve(reminder, cache)
            cache[reminder] = s
        ans = min(ans, 1 + s) 
    return ans

assert 1 == solve(1)
assert 3 == solve(12)
assert 2 == solve(13)
assert 2 == solve(130)

