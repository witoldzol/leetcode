from typing import List
# nums = [1,2,3]
# k = 1
# final  = [3,1,2]
nums = [1,2,3,4,5,6,7]
k = 3
expected = [5,6,7,1,2,3,4]
class Solution:
    def reverse_list(self, arr: list):
        le = len(nums)
        l = 0
        r = le - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        print(nums)
        self.reverse_list(nums)
        print(nums)
        # reverse entire array - in place

res = Solution().rotate(nums,k)
print(res)
assert expected == res

