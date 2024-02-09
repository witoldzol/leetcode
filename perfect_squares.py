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


assert 1 == wrapper(1)
assert 3 == wrapper(12)
assert 2 == wrapper(13)
# assert 2 == solve(1300)

