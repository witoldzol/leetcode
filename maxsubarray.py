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

    def middle_to_left(self, nums: List[int] ) -> int:
        current_sum = 0
        maximum = nums[0]
        for x in reversed(nums):
            current_sum += x
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def middle_to_right(self, nums: List[int] ) -> int:
        current_sum = 0
        maximum = nums[0]
        for x in nums:
            current_sum += x
            if current_sum > maximum:
                maximum = current_sum
        return maximum


    def split(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        left_split = self.split(left)
        right_split = self.split(right)
        cross_left = self.middle_to_left(left)
        cross_right = self.middle_to_right(right)
        return max(left_split, right_split, cross_left + cross_right, cross_left, cross_right)

    def start_to_middle(self, nums: List[int], start: int, end: int) -> int:
        current_sum = 0
        maximum = nums[start]
        for x in reversed(range(start, end + 1)):
            current_sum += nums[x]
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def middle_to_end(self, nums: List[int], start: int, end: int ) -> int:
        current_sum = 0
        maximum = nums[start]
        for x in range(start, end):
            current_sum += nums[x]
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def split_i(self, nums: List[int], start: int, end: int) -> int:
        if start > end:
            raise Exception(f"start is bigger than end, fix it ! {start=} {end=}")
        if start == end:
            return nums[start]
        middle = (start + end) // 2
        left_split = self.split_i(nums, start, middle)
        if middle + 1 == end:
            right_split = self.split_i(nums, middle + 1, end)
        else:
            right_split = self.split_i(nums, middle, end)
        cross_left = self.start_to_middle(nums, start, middle)
        if middle + 1 == end:
            cross_right = self.middle_to_end(nums, middle, end)
        else:
            cross_right = self.middle_to_end(nums, middle, end)
        return max(left_split, right_split, cross_left + cross_right, cross_left, cross_right)
