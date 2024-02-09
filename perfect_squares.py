import math
def perfect_squares(n: int) -> int:
    reminder = n
    counter = 0
    while reminder:
        sq = math.sqrt(reminder)
        print(f"{sq=}")
        if sq % reminder == 0:
            return counter + (reminder // sq)
        else:
            print(f"BEFORE {reminder=} ")
            print(f"{math.floor(sq)=}")
            reminder = reminder - pow(math.floor(sq), 2)
            print(f"reminder for {sq=} is {reminder=}")
            counter += 1
            print(f"{reminder=}")
    return counter

print( perfect_squares(12))
    

# assert 3 == perfect_squares(12)
# assert 2 == perfect_squares(13)
