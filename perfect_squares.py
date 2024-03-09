import math


# sq or 1 is 1
# sq of 2 is 2 * 1
# sq of 3 is 3 * 1 or ? other per sq? no
# sq of 4 is 4 * 1 or 2*2
# sq of 5 is sq(4) + sq(1) or 4 * sq(1)
# sq of 6 is sq(4) + sq(2)
# sq of 7 is sq(4) + sq(o3)
# sq of 8 is sq(4) * 2
# sq of 9 is
#   9 * sq(1)
#   2 * sq(4) + sq(1)
#   1 * sq(9) + sq(0)
#
# n = 12
# i = 1, m = 1, r =0, c[1] = 1 + 0
# i = 2, m = 1, r = 1 , res = 1 + 1
# i = 3, m = 1, r = 1 + 2
# i = 4 , m = 2
#   j = 1, r = 3, (1 + 3)
#   j = 2, r = 0 ( 1 + 0) => overwrite previous  result
# i = 5, m = 2
#   j = 1 r = 4 ( 1 + 2)
#   j = 2 r = 1 ( 1 + 1)
#
# i = 6, m = 2
#   j = 1, r = 5, (1 + 2)
#   j = 2 , r = 2 ( 1 + )
#
def iter(n: int) -> int:
    cache = [float("inf")] * (n + 1)
    cache[0] = 0
    for i in range(1, n + 1):
        middle = math.floor(i**0.5)
        for j in range(1, middle + 1):
            reminder = i - (j * j)
            cache[i] = min(cache[i], 1 + cache[reminder])
    return cache[n]


assert 3 == iter(12)
assert 2 == iter(13)
assert 2 == iter(800)
