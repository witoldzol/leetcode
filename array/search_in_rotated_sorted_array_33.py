# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
import pudb

from typing import List

nums = [4,5,6,7,0,1,2]

def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"{low=} {mid=} {high=}")
        if nums[mid] == target:
            return mid
        elif nums[mid] > target: # 6, we need 4
            high = mid-1
        else:
            low = mid+1
    return -1

def binary_search(nums: List[int], target: int, low: int = 0, high = 0) -> int:
    if not high:
        high = len(nums)
    while low <= high:
        mid = (low + high) // 2
        print(f"{low=} {mid=} {high=}")
        if nums[mid] == target:
            return mid
        elif nums[mid] > target: # 6, we need 4
            high = mid-1
        else:
            low = mid+1

def solve(nums: List[int], target: int) -> int:
    # we know that if we split list in half, at least one half will be sorted
#   if the sorted list contains the target number, we can just do binary search on it
#   if not, split the other list in half again, and recheck
    # split until we find the target inside in sorted half 
    # split in half
    middle = len(nums) // 2
    # figure out if the left side is in order
    # # LEFT in order
    # if nums[0] <= nums[middle]:
    #     # TARGET INSIDE 
    #     if target <= nums[middle]: # target in left side
    #         return binary_search(nums, target, 0, middle)
    # # RIGHT in order
    # else:
    #     # TARGET INSIDE 
    #     if target >= nums[middle]:
    #         return binary_search(nums[middle:], target, middle, len(nums))
    #
    # check if left is sorted
    if nums[0] <= nums[middle]:
        if target <= nums[middle]: # target in left side
            return binary_search(nums, target, 0, middle)
        else: # left is sorted, but doesn't contain the target, drop left and split again
            return solve(nums[middle:], target)
    # right is sorted
    else:
        if target >= nums[middle]: # if target in right side, return
            return binary_search(nums, target, middle, len(nums))
        else: # right is sorted but doesn't contain target, drop right and split again on left
            return solve(nums[:middle + 1], target)
