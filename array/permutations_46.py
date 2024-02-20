# https://leetcode.com/problems/permutations/description/
from typing import List

nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permutate(nums: List[int]) -> List[List[int]]:
    results = []
    # base condition
    if len(nums) == 1:
        return [nums[:]]
    for _ in range(len(nums)):
        # get first element
        n = nums.pop(0)
        #   generate permutations - results become input 
        perms = permutate(nums)
        # append n back to results
        for p in perms:
            p.append(n)
        # resuts
        results.extend(perms)
        # add n back, otherwise we run out of digits in n before loop ends
        nums.append(n)
    return results


input = [1,2,3]

def per(nums: List[int]) -> List[List[int]]:
    results = []
    # lets start with array reversal
    if len(nums) == 1:
        return [nums[:]]
    for _ in range(len(nums)):
        x = nums.pop(0)
        permutations = per(nums)
        for p in permutations:
            p.append(x)
        results.extend(permutations)
        nums.append(x)
    return results

print(per(input))


