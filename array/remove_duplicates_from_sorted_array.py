from typing import List

# input = [0,0,1,1,1,2,2,3,3,4]
# expected = 5
input = [1]
expected = 1
# input = [1,2]
# expected = 2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 0
        prev = None
        current_idx = 0
        for x in nums:
            if x == prev:
                continue
            else:
                nums[current_idx] = x
                prev = x
                current_idx += 1
                unique_count += 1
                if current_idx >= len(nums):
                    break
        return unique_count


assert Solution().removeDuplicates(input) == expected


