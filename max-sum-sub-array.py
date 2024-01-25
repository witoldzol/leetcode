# https://leetcode.com/problems/max-pair-sum-in-an-array/solutions/3902240/using-map-detailed-approach-and-easy-to-understand-code/
from typing import List

nums = [31, 25, 72, 79, 74]
# nums = [8,75,28,35,21,13,21]
nums = [84, 91, 18, 59, 27, 9, 81, 33, 17, 58]


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        total_max = -1
        max_val = {}
        for i, x in enumerate(nums):
            x_s = str(x)
            x_arr = [*x_s]
            x_max = int(max(x_arr))
            if x_max not in max_val:
                max_val[x_max] = [(i, x)]
            else:
                if i != max_val[x_max][0]:
                    max_val[x_max].append((i, x))
        for item in max_val.values():
            print(item)
            if len(item) >= 2:
                item_sorted = sorted(item, key=lambda x: x[1], reverse=True)
                temp = 0
                for i, v in item_sorted[:2]:
                    temp += v
                if temp > total_max:
                    total_max = temp
        return total_max


print(Solution().maxSum(nums))
