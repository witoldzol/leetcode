# https://leetcode.com/problems/maximum-subarray/description/

from typing import List, Tuple
from sys import maxsize

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [1, -1, 2, 1]
nums = [-1, 3, 2, -1]


class Solution:
    def brute_force(self, nums: List[int]) -> int:
        maximum = 0
        for ix, x in enumerate(nums):
            for iy, y in enumerate(nums):
                sum = 0
                for z in nums[ix:iy]:
                    sum += z
                if sum > maximum:
                    maximum = sum
        return maximum

    def brute_force_cache(self, nums: List[int]) -> int:
        maximum = 0
        for ix, x in enumerate(nums):
            cache = 0
            for y in nums[ix:]:
                sum = cache + y
                cache = sum
                if sum > maximum:
                    maximum = sum
        return maximum

    def brute_force_with_pointers(self, nums: List[int]):
        max_sum = -maxsize
        sum = 0
        # skip zeros, reset sum if sum goes to zero or below
        for x in nums:
            if x == 0:
                continue
            if x < 0:
                sum += x
                if sum > max_sum:
                    max_sum = sum
                if sum <= 0:
                    sum = 0
            else:
                sum += x
                if sum > max_sum:
                    max_sum = sum
        return max_sum

    def brute_force_with_pointers_slim(self, nums: List[int]):
        maximum = nums[0]
        sum = 0
        for n in nums:
            if sum < 0: # if there is only one element, it will be taken instead of 0
                sum = 0
            sum += n
            maximum = max(sum, maximum)
        return maximum
