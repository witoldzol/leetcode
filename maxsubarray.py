# https://leetcode.com/problems/maximum-subarray/description/

from typing import List, Tuple

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [1, -1, 2, 1]
nums = [-1, 3, 2, -1]


class Solution:

    def brute_force(self, nums: List[int]) -> int:
        maximum = 0
        for ix, x in enumerate(nums):
            for iy, y in enumerate(nums):
                sum = 0
                for z in nums[ix:iy]:
                    sum += z
                if sum > maximum:
                    maximum = sum
        return maximum

    def brute_force_cache(self, nums: List[int]) -> int:
        maximum = 0
        for ix, x in enumerate(nums):
            cache = 0
            for y in nums[ix:]:
                sum = cache + y
                cache = sum
                if sum > maximum:
                    maximum = sum
        return maximum

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
        ll = left[lmm:]
        rr = right[:rmm]
        llrr = sum(ll + rr)
        # alternative
        if len(left) % 2 != 0 and len(left) != 1:
            ll = left[lmm - 1 :]
        if len(right) % 2 != 0 and len(right) != 1:
            rr = right[: rmm + 1]
        alternative_llrr = sum(ll + rr)
        print(f"middle is = {ll + rr}")
        if llrr > m:
            m = llrr
        if alternative_llrr > m:
            m = alternative_llrr
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
        return (ls + rs), m

    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer
        return self.split(nums, 0)[1]


Solution().maxSubArray(nums)
