# https://leetcode.com/problems/permutations/description/

from typing import List

nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def per(nums: List[int]) -> List[List[int]]:
    result = []
    for i in range(len(nums)):
        result.append(per(nums[i:nums]))


