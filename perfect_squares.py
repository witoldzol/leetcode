import math

def perfect_squares(n: int):
    results = [-1] * (n + 1)
    results[0] = 0
    results[1] = 1
    def solve(n):
        if n == 0:
            return 0
        if n < 0:
            raise Exception(f'Negative number detected {n}')
        if results[n] != -1:
            return results[n]
        sqr = n ** 0.5
        middle = math.floor(sqr)
        ans = float('inf')
        for i in range(1, middle + 1): # include outer bound
            reminder = n - i*i
            ans = min(ans, solve(reminder) + 1)
        results[n] = ans
        return ans
    return solve(n)

# 12 = 1 * 12, 2*2 = 4 * 3, 3*3 = 9, + 1*3 =4
# we need to find a combination of perfect squares that adds up to the lowest number
def iterative(n: int):
    results = [float('inf')] * (n + 1)
    results[0] = 0
    sqr = n ** 0.5
    middle = math.floor(sqr)
    for i in range(1, n + 1):
        for j in range(1, middle + 1):
            reminder = i - j * j
            results[i] = min(results[i], 1 + results[reminder])
    return results[n]

def numSquares(n: int) -> int:
    # memo = [float('inf')] * (n + 1)
    memo = [float('inf')] * (n + 1)
    memo[0] = 0

    sqr = n ** 0.5
    middle = math.floor(sqr)
    for i in range(1, n + 1):
        j = 1
        for j in range(1, middle + 1):
            memo[i] = min(memo[i], 1 + memo[i - j * j])
            
    return memo[n]

# print(f"solution = {perfect_squares(12)}")
# assert 3 == perfect_squares(12)
# assert 2 == perfect_squares(13)
# assert 2 == perfect_squares(800)
assert 3 == iterative(12)
assert 2 == iterative(13)
assert 2 == iterative(800)

assert 3 == numSquares(12)
assert 2 == numSquares(13)
assert 2 == numSquares(800)
