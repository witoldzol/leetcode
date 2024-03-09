# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
import pudb

from typing import List

nums = [4, 5, 6, 7, 0, 1, 2]


def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"{low=} {mid=} {high=}")
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:  # 6, we need 4
            high = mid - 1
        else:
            low = mid + 1
    return -1


def my_search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] == target:
            return middle
        # if left sorted
        if nums[low] <= nums[middle]:
            # is target in the left part?
            if nums[low] < target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
        else:  # right is sorted
            # does it have a target?
            if nums[middle] < target < nums[high]:
                low = middle + 1
            else:
                high = middle - 1
    return -1


# nums = [4,5,6,7,0,1,2]
print(my_search(nums, 0))
