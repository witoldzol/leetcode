# https://leetcode.com/problems/3sum/description/
# return all 3 digits that add up to 0, no duplicates, all digits should be diff from each other
from typing import List

input = [-1,0,1,2,-1,-4]
input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

# def three_sum(nums: List[int]):
#     ans=set()
#     nums.sort()
#     n=len(nums)
#     for i in range(n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):
#                 temp=nums[i]+nums[j]+nums[k]
#                 if temp==0:
#                     ans.add((nums[i],nums[j],nums[k]))
#     return ans

def three_sum(nums: List[int]):
    ans=set()
    nums.sort()
    for ix, x in enumerate(nums):
        for iy, y in enumerate(nums):
            for iz, z in enumerate(nums):
    # for  x in nums:
        # for y in nums:
            # for z in nums:
                if x ==-1 and y == 0:
                    print('yes')
                if x + y + z == 0:
                    if ix != iy and ix != iz and iy != iz:
                        a = sorted([x,y,z])
                        k,p,o = a
                        ans.add((k,p,o))
    return ans
three_sum(input)
# print(f"solution {three_sum(input)}")
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

def test_three_sum():
    assert len(expected) == len(three_sum(input))

