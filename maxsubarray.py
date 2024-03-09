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
            if sum < 0:  # if there is only one element, it will be taken instead of 0
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
            if sum < 0:  # we look backwards
                sum = 0
                if i < len(nums):
                    start = i
            sum += n
            if sum >= maximum:
                maximum = sum
                end = i
        return maximum, start, end

    def middle_to_left(self, nums: List[int]) -> int:
        current_sum = 0
        maximum = nums[0]
        for x in reversed(nums):
            current_sum += x
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def middle_to_right(self, nums: List[int]) -> int:
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
        return max(
            left_split, right_split, cross_left + cross_right, cross_left, cross_right
        )

    def start_to_middle(self, nums: List[int], start: int, end: int) -> int:
        current_sum = 0
        maximum = nums[start]
        for x in reversed(range(start, end + 1)):
            current_sum += nums[x]
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def middle_to_end(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return nums[start]
        current_sum = 0
        maximum = nums[start]
        for x in range(start, end):
            current_sum += nums[x]
            if current_sum > maximum:
                maximum = current_sum
        return maximum

    def maxCrossingSum(self, arr, l, m, h):
        # left
        sm = 0
        left_sum = -10000
        for i in range(m, l - 1, -1):
            sm = sm + arr[i]
            if sm > left_sum:
                left_sum = sm
        # right
        sm = 0
        right_sum = -1000
        for i in range(m, h + 1):
            sm = sm + arr[i]
            if sm > right_sum:
                right_sum = sm
        return max(
            left_sum + right_sum - arr[m], left_sum, right_sum
        )  # why - arr[m] ????

    def split_i(self, nums: List[int], start: int, end: int) -> int:
        print(f"starting split function, {start=}, {end=}")
        if start > end:
            return -(10**4)
            # raise Exception(f"start is bigger than end, fix it ! {start=} {end=}")
        if start == end:
            print(
                f"Start == End {start=}; End of function, returning {nums[start - 1]}"
            )
            print("==================================================")
            return nums[start - 1]
        middle = (start + end) // 2
        print(f"{middle=}")
        left_split = self.split_i(nums, start, middle - 1)
        right_split = self.split_i(nums, middle + 1, end)
        cross = self.maxCrossingSum(nums, start, middle, end)
        result = max(left_split, right_split, cross)
        print(f"End of function, returning max of {result}")
        print("==================================================")
        return result


def find_max(arr):
    # iterate ove the array, keep adding the numbers, if the sum ever dips below zero, reset the pointer
    sum = 0
    maximum = -(10**4)
    for x in arr:
        if (
            sum < 0
        ):  # it's important to check before we add new one, this way we look back and not ahead
            sum = 0
        sum += x
        if sum > maximum:
            maximum = sum
    return maximum
