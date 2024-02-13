# https://leetcode.com/problems/3sum/description/
# return all 3 digits that add up to 0, no duplicates, all digits should be diff from each other
from typing import List

input = [-1,0,1,2,-1,-4]
input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

def three_sum(input: List[int]):
    results = set()
    for ix, x in enumerate(input):
        for iy, y in enumerate(input):
            for iz, z in enumerate(input):
                if x + y + z == 0 and ix != iy and ix != iz and iy != iz:
                    x, y ,z = sorted([x,y,z])
                    results.add((x,y,z))
    return [list(x) for x in results]

print(f"solution {three_sum(input)}")
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

def test_three_sum():
    assert len(expected) == len(three_sum(input))

