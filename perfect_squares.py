def perfect_squares(n: int) -> int:
    import math
    x = math.floor(math.sqrt(n))
    reminder = None
    counter = 0
    if n % x == 0:
        return n // x
    else:
        counter += n // x
        reminder = n - (counter * x)
    print(f"{reminder=}")
    print(x)

perfect_squares(13)

# assert 3 == perfect_squares(12)
# assert 2 == perfect_squares(13)
