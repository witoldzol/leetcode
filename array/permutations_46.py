# https://leetcode.com/problems/permutations/description/
from typing import List

nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def per(nums: List[int]) -> List[List[int]]:
    results = []
    if len(nums) == 1:
        return [nums[:]]
    for i in range(len(nums)):
        n = nums.pop(0)
        #   generate permutations
        perms = per(nums)
        # append n back to results
        for p in perms:
            p.append(n)
        # resuts
        results.extend(perms)
        # add n back
        nums.append(n)
    return results
