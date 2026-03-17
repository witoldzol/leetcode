from typing import List

def is_increasing(nums, skip = None)->int:
    if len(nums) < 2:
        return True
    prev = None
    for idx, x in enumerate(nums):
        if idx == skip:
            continue
        if prev is None:
            prev = x
            continue
        if x <= prev:
            return idx - 1
        prev = x
    return -1

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        i = is_increasing(nums)
        if i == -1:
            return True
        left = i
        right = i+1
        left_result = is_increasing(nums, left)
        right_result = is_increasing(nums, right)
        if left_result == -1 or right_result == -1:
            return True
        return False

n = [1,2,10,5,7]
n = [2,3,1,2]
r = Solution().canBeIncreasing(n)
print(r)

