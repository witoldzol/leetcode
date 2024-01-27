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

    def slim(self, nums: List[int]):
        maximum = nums[0]
        sum = 0
        for n in nums:
            if sum < 0: # if there is only one element, it will be taken instead of 0
                sum = 0
            sum += n
            maximum = max(sum, maximum)
        return maximum

    def slim_with_indexes(self, nums: List[int]):
        maximum = nums[0]
        sum = 0
        start = 0
        end = 0
        for i, n in enumerate(nums):
            if sum < 0: # we look backwards
                sum = 0
                if i < len(nums):
                    start = i
            sum += n
            if sum >= maximum:
                maximum = sum
                end = i
        return maximum, start, end

    def find_max_left(self, arr: List[int]) -> int:
        current_sum = 0
        maximum = -10**4
        print(f"going from mid to left for array {arr}")
        for x in reversed(arr):
            current_sum += x
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def find_max_right(self, arr: List[int]) -> int:
        current_sum = 0
        maximum = -10**4
        for x in arr:
            current_sum += x
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def divide(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        mid = len(nums) // 2
        left =  nums[:mid]
        right = nums[mid:]
        l = self.divide(left)
        r = self.divide(right)
        max_left = self.find_max_left(left)
        max_right = self.find_max_right(right)
        m = max(max_left + max_right, max_left, max_right)
        return max(l,r,m)
