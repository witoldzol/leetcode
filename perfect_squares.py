import math
def perfect_squares(n: int) -> int:
    sq = math.sqrt(n)
    counter = 0
    if sq % n == 0:
        return n // sq
    else:
        counter += 1
        reminder = n - (math.floor(sq) * math.floor(sq))
        print(f"{reminder=}")

perfect_squares(13)
    

# assert 3 == perfect_squares(12)
# assert 2 == perfect_squares(13)
