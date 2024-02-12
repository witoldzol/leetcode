# https://leetcode.com/problems/container-with-most-water/description/

from typing import List

input = [1,8,6,2,5,4,8,3,7]
input = [1,1]
input = [2,3,10,5,7,8,9]

def water(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    maximum = 0
    while left != right:
        print(f"start = {left=} and {right=}")
        width = right - left
        height = min(nums[left], nums[right])
        area = width * height
        if area > maximum:
            maximum = area
        left += 1
        if left == right:
            return maximum
        width = right - left
        print(f"after adding 1 to left we have {left=} and {right=}")
        height = min(nums[left], nums[right])
        area = width * height
        if area > maximum:
            maximum = area
        right -= 1
        if left == right:
            return maximum
        print(f"after removing 1 from right we have {left=} and {right=}")
        width = right - left
        height = min(nums[left], nums[right])
        area = width * height
        if area > maximum:
            maximum = area
    return maximum




print(f"solution = {water(input)}")
assert 36 == water(input)

