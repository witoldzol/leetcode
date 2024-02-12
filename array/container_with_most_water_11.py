# https://leetcode.com/problems/container-with-most-water/description/

from typing import List

input = [1,8,6,2,5,4,8,3,7]
input = [1,1]
input = [2,3,10,5,7,8,9]

def water(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    maximum = 0
    while left < right:
        width = right - left
        lower_height = min(nums[left], nums[right])
        if nums[left] < nums[right]: # this is the crucial part -> we move only the lower line
            left += 1
        else:
            right -= 1
        maximum = max(maximum, width * lower_height)
    return maximum

print(f"solution = {water(input)}")
assert 36 == water(input)

