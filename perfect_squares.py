import math

def solve(n: int):
    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    max_range = math.floor(n ** 0.5)
    ans = float('inf')
    for i in range(1, max_range + 1):
        reminder = n - (i*i)
        s = solve(reminder)
        ans = min(ans, 1 + s) 
    return ans


assert 1 == solve(1)
assert 3 == solve(12)
assert 2 == solve(13)
