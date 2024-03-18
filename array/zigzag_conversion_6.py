# https://leetcode.com/problems/zigzag-conversion/
from typing import Tuple

def get_counter(curr: int, max: int, direction: int) -> Tuple[int, int]:
    max -= 1
    if curr == -1:
        print(f"got -1, returning curr = 0")
        return 0, 1
    if curr == max:
        direction = -1
    if curr == 0:
        direction = 1
    return curr + direction, direction

def convert(s: str, numRows: int) -> str:
    ars = {}
    for i in range(numRows):
        ars[i] = []
    print(ars)
    direction = 1
    counter = -1
    for char in s:
        print(f"{numRows=}")
        counter, direction = get_counter(counter, numRows, direction)
        print(f"im in loop, curr is {counter}")
        ars[counter].append(char)
    result = ""
    for v in ars.values():
        result += (''.join(v))
    return result

result = convert("PAYPALISHIRING",3)
assert "PAHNAPLSIIGYIR" == result

