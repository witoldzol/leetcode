# https://leetcode.com/problems/permutations/description/
import pudb

from typing import List

nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def per(nums: List[int]) -> List[List[int]]:
    pu.db
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

# def my_per(nums: List[int]) -> List[List[int]]:
#     # base condition
#     if len(nums) == 1:
#         # return a copy of the array
#         return [nums[:]]
#     for _ in nums: 
#         # remove first element
#         x = nums.pop(0)
#         # repeat until you get 1 len
#         subarrs = my_per(nums)
#         # iterate over sub arrays
#         for s in subarrs:
#
# # 3 iterations
# nums = [1,2,3]
# i = 0
#     x = 1
#     sub = perm([2,3])
        # iterate 2 times
#       i = 0
#           x = 2
    #       sub = perm([3])
#               len == 1
#               return copy of [3] in a list
#           sub = [[3]]
#           for p in sub
#               [3].append(2) -> [3,2]
#
#

# print(per(nums))
# print(f"{output}")
# assert per(nums).sort() == output.sort()


def bob(nums):
    res = []
    if len(nums) == 1:
        return [nums[:]]
    x = nums.pop(0)
    y = bob(nums)
    for yy in y:
        yy.append(x)
    res.extend(y)
    return res

print(bob(nums))
