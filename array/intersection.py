from typing import List
# a = [4,9,5]
# b = [9,4,9,8,4]
a = [1,2,3]
b = [2,4,5,6]
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for x in nums1:
            for idx, y in enumerate(nums2):
                if x < y:
                    break
                elif x == y:
                    print('x', x)
                    print('y', y)
                    result.append(x)
                    nums2[idx] = -1
                    break
        return result

print(Solution().intersect(a,b))
