# https://leetcode.com/problems/container-with-most-water/description/

from typing import List

input = [1,8,6,2,5,4,8,3,7]

def water(nums: List[int]) -> int:
    heights = []
    for ix, x in enumerate(nums):
        heights.append((x,ix))
    sorted_heights = sorted(heights, key=lambda x: x[0], reverse=True)
    print(sorted_heights)
    sorted_width = sorted(heights, key=lambda x: x[1], reverse=True)
    print(sorted_width)
    for h in sorted_heights:
        for w in sorted_width:
            if h[1] != w[1]:
                return abs(h[1] - w[1]) * min(h[0],w[0])

print(f"solution = {water(input)}")

