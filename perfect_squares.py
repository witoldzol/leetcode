import math
def perfect_squares(n: int):
    results = [0] * (n + 1)
    results[0] = 0
    results[1] = 1
    def solve(n):
        if n == 0:
            return 0
        if n < 0:
            raise Exception(f'Negative number detected {n}')
        # for every i between 1 and n ( inclusive )
        # check for perfect squares ( 1 to floor(sq_root(i))) or i*i <= n
        for i in range(1, n + 1):
            sqr = n ** 0.5
            print(f"{i=}")
            for j in range(1, math.floor(sqr) + 1): # also inclusive
                print(f"{j=}")
                reminder = n - (j * j)
                if results[j] != 0:
                    sol = results[j]
                else:
                    sol = min(results[j], solve(reminder) + 1)
                    results[j] = sol
        return results[n]

print(perfect_squares(4))
