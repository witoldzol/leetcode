# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = 0
        max_i = None
        # brute force 
        for ix, x in enumerate(nums):
            for iy, y in enumerate(nums[ix:]):
                temp = 0
                for q in nums[ix:iy+1]:
                    temp += q
                    print(f"subarray is {nums[ix:iy+1]}")
                if temp > max:
                    max = temp
        print(max)

Solution().maxSubArray(nums)
