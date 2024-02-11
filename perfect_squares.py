import math



def iter(n: int ) -> int:
    cache = [float('inf')] * (n + 1)
    cache[0] = 0
    for i in range(1, n+1):
        middle = math.floor(i ** 0.5)
        for j in range(1, middle + 1):
            reminder = i - (j * j)
            cache[i] = min(cache[i], 1 + cache[reminder])
    return cache[n]

assert 3 == iter(12)
assert 2 == iter(13)
assert 2 == iter(800)
