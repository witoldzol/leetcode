# https://leetcode.com/problems/container-with-most-water/description/

from typing import List

input = [1,8,6,2,5,4,8,3,7]

def water(nums: List[int]) -> int:
    max = 0
    for ix, x in enumerate(nums):
        for iy, y in enumerate(nums):
            if ix==iy:
                continue
            max_water = (iy - ix) * min(x,y) 
            if max_water > max:
                max = max_water
    return max

print(f"solution = {water(input)}")

