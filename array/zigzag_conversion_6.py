# https://leetcode.com/problems/zigzag-conversion/
from typing import Tuple

def get_counter(curr: int, max: int, direction: int) -> Tuple[int, int]:
    max -= 1
    if curr == -1:
        return 0, 1
    if curr == max:
        direction = -1
    if curr == 0:
        direction = 1
    return curr + direction, direction

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    ars = {}
    for i in range(numRows):
        ars[i] = []
    direction = 1
    counter = -1
    for char in s:
        counter, direction = get_counter(counter, numRows, direction)
        ars[counter].append(char)
    result = ""
    for v in ars.values():
        result += (''.join(v))
    return result

result = convert("PAYPALISHIRING",3)
assert "PAHNAPLSIIGYIR" == result

result = convert("AB",1)
assert "AB" == result

