from dataclasses import dataclass

input = [0,1,0,3,12]
input = [0,0]

def move_zeros(input: list[int]) -> list[int]:
    if len(input) == 1:
        return input
    l = 0
    r = 1
    while l < len(input) and r < len(input):
        if input[l] == 0:
            if input[r] != 0:
                # swap
                input[l],input[r] = input[r],input[l]
                l += 1
                r += 1
            else:
                r += 1
        elif input[l] != 0:
            if input[r] != 0:
                l += 1
                r += 1
            else:
                l += 1
    return input

print(move_zeros(input))

