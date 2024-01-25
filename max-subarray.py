# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = 0
        maxi = None
        for ix, x in enumerate(nums):
            print(f"====> i is {x}")
            for iy, y in enumerate(nums[ix+1:]):
                sum = 0
                for z in nums[ix+1:-iy]:
                    print(f"z is {z}")
                    sum += z
                print("==========")
                if sum > max:
                    max = sum
                    maxi = (ix,iy)
        print(f"Max sub is {max}, index {maxi}")

Solution().maxSubArray(nums)
