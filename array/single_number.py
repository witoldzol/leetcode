input = [1,2,1,2,4]
expected = 4

class Solution():
    def do(self, nums):
        r = 0
        for x in nums:
            r ^= x
        return r

assert Solution().do(input) == expected
