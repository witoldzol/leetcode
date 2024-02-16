# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
import pudb

from typing import List

nums = [4,5,6,7,0,1,2]
nums = [0,1,2,4,5,6,7]

def binary_search(nums: List[int], target: int) -> int:
    # pu.db
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

def solve(nums: List[int], target: int) -> int:
    pass
    # we know that if we split list in half, at least one half will be sorted
#   if the sorted list contains the target number, we can just do binary search on it
#   if not, split the other list in half again, and recheck

# print(solve(input, 4))
