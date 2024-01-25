# https://leetcode.com/problems/maximum-subarray/description/

from typing import List, Tuple

nums = [-2,1,-3,4,-1,2,1,-5,4]

# BRUTE FORCE SOUTION N^3
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max = 0
#         maxi = None
#         for ix, x in enumerate(nums):
#             print(f"====> i is {x}")
#             for iy, y in enumerate(nums[ix+1:]):
#                 sum = 0
#                 for z in nums[ix+1:-iy]:
#                     print(f"z is {z}")
#                     sum += z
#                 print("==========")
#                 if sum > max:
#                     max = sum
#                     maxi = (ix,iy)
#         print(f"Max sub is {max}, index {maxi}")

class Solution:
    def merge(self, left: List[int], right: List[int]):
        return left + right

    def split(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            print(f"got to the bottom, {nums=}")
            return nums
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        return self.split(left) + self.split(right)

    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer
        print( self.split(nums))

Solution().maxSubArray(nums)
