from typing import List
nums = [1,2]
k = 1
expected = [1,2]
expected = [2,1]
class Solution:
    def reverse_list(self, nums: list, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        if k >= len(nums):
            k = k % len(nums)
        self.reverse_list(nums, 0 , len(nums) - 1)
        self.reverse_list(nums, 0 , k - 1)
        self.reverse_list(nums, k , len(nums) - 1)

Solution().rotate(nums,k)
print(f"nums: {nums}")
assert expected == nums
