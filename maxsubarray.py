# https://leetcode.com/problems/maximum-subarray/description/

from typing import List, Tuple

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
    # if we find a negative number, continue
    # if we find positive, save index as first_pointer, keep track of sum
    # if we find subsequent negative number, keep going, update sum
    # if we find a positive number, and it is bigger than current sum, update first_pointer to this index
    # if the positive number is smaller, keep going, update sum
    # at any point, check if sum > maximum. if yes, save index in second_pointer
    #
    # you should be done with a single pass
        start_index = 0
        max_index_start = 0
        max_index_end = 0
        max_sum = 0
        sum = 0
        # initiate start index
        for i, x in enumerate(nums):
            if x < 1:
                continue
            else:
                start_index = i
                max_index_start = i
                sum = x
                max_sum = x
                break
        # meat and potatoes 
        for ix, x in enumerate(nums):
            if x == 0:
                continue
            if x < 0:
                sum += x
            else:
                # check if current value beats the current sum - in case previous value was negative
                if x > sum:
                    # set new max if x can beat it
                    if x > max_sum:
                        max_sum = x
                        max_index_start = ix
                    # set a new start pointer
                    sum = x
                    start_index = ix
                else:
                    sum += x
                    if sum > max_sum:
                        max_sum = sum
                        max_index_end = ix
        return max_sum
