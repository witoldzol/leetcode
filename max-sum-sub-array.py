# https://leetcode.com/problems/max-pair-sum-in-an-array/solutions/3902240/using-map-detailed-approach-and-easy-to-understand-code/
from typing import List
nums = [31,25,72,79,74]
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        solution = -1
        for i in nums:
            for j in nums:
                if i == j:
                    continue
                i_s = str(i)
                j_s = str(j)
                i_set = {x for x in i_s}
                j_set = {y for y in j_s}
                max_i = max(i_set)
                max_j = max(j_set)
                if max_i == max_j:
                    sum = i + j
                    if sum > solution:
                        solution = sum
        return solution

print(Solution().maxSum(nums))
