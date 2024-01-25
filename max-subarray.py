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
        maxx = 0
        if len(nums) < 2:
            print(f"got to the bottom, {nums=}")
            if not nums:
                if nums[0] > maxx:
                    maxx = nums[0]
            return nums, maxx
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        l_sum = sum(left)
        if l_sum > maxx:
            maxx = l_sum
        r_sum = sum(right)
        if r_sum > maxx:
            maxx = r_sum
        lm = left[-1]
        rm = right[0]
        lr = [lm]+[rm]
        lm_sum = sum(lr)
        if lm_sum > maxx:
            maxx = lm_sum
        l_split, l_max = self.split(left)
        r_split, r_max = self.split(right)
        return (l_split + r_split, max(maxx,l_max, r_max))

    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer
        print( self.split(nums))

Solution().maxSubArray(nums)
