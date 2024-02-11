import math
def perfect_squares(n: int):
    results = [float('inf')] * (n + 1)
    results[0] = 0
    results[1] = 1
    def solve(n):
        if n == 0:
            return 0
        if n < 0:
            raise Exception(f'Negative number detected {n}')
        sqr = n ** 0.5
        middle = math.floor(sqr)
        ans = float('inf')
        for i in range(1, middle + 1): # include outer bound
            reminder = n - i*i
            ans = min(ans, solve(reminder) + 1)
        return ans
    return solve(n)


print(f"solution = {perfect_squares(12)}")
assert 3 == perfect_squares(12)
assert 2 == perfect_squares(13)
