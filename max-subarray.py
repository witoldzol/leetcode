# https://leetcode.com/problems/maximum-subarray/description/

from typing import List, Tuple

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1,-1,2,1]
nums = [-1,3,2,-1]

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

    def split(self, nums: List[int], m: int) -> Tuple[List[int], int]:
        if len(nums) < 2:
            # print(f"got to the bottom, {nums=}")
            s = sum(nums)
            if s > m:
                m = s
            return nums, m
        middle = len(nums) // 2
        left = nums[:middle]
        l_s = sum(left)
        right = nums[middle:]
        r_s = sum(right)
        lmm = len(left) // 2
        rmm = len(right) // 2
        ll = left[-lmm+1:]
        rr = right[:rmm+1]
        llrr = sum(ll+rr)
        print(f"middle is = {ll + rr}")
        if llrr > m:
            m = llrr
        ls, lm = self.split(left, m) 
        rs, rm = self.split(right, m)
        if l_s > m:
            m = l_s
        if r_s > m:
            m = r_s
        if lm > m:
            m = lm
        if rm > m:
            m = rm
        # print(f"{llrr=}, {l_s=}, {r_s=}, {lm=}, {rm=}")
        return  (ls+rs), m

    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer
        print( self.split(nums, 0))

Solution().maxSubArray(nums)
