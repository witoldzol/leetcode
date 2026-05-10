class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        maximum = nums[0]
        current = 0
        for n in nums:
            if current + n < 0:
                current = 0
                continue
            current += n
            if current > maximum:
                maximum = current
        return maximum
