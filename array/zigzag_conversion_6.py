# https://leetcode.com/problems/zigzag-conversion/

def convert(s: str, numRows: int) -> str:
    ars = {}
    for i in range(numRows):
        ars[f"array{i}"] = []
    for a in ars:
        print(a)

convert("BOB", 4)

