# https://leetcode.com/problems/3sum/description/
# return all 3 digits that add up to 0, no duplicates, all digits should be diff from each other
from typing import List

input = [-1, 0, 1, 2, -1, -4]
# input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# input = [-1,0,1,1]
# for i in 0,3
# i = 0
# j = 0 + 1
# k = 3
# j < k true
# temp = -1 (0) + 0 (1) + (1) -> 0
# add (-1,0,1) j +=1, j = 2
#
# temp = -1 (0) + 1 (2) + (1) -> 0


def three_sum(nums: List[int]):
    ans = set()
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if temp == 0:
                ans.add((nums[i], nums[j], nums[k]))
                j += 1  # we can move on, because there is only one number that can match this condition, so we can leave
            elif temp > 0:
                k -= 1
            else:
                j += 1
    return ans


def complement(input):
    r = set()
    # split sets into negative, positive and zeros list
    p = []
    n = []
    Z = []
    for x in input:
        if x > 0:
            p.append(x)
        elif x < 0:
            n.append(x)
        else:
            Z.append(x)
    P = set(p)
    N = set(n)
    # edge case with 3 or more zeros
    if len(Z) > 2:
        r.add((0, 0, 0))
    # complement of zeros
    if len(Z):
        for f in P:
            if -f in N:
                r.add((-f, 0, f))
    # complement of 2s positive
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            two_sum = p[i] + p[j]
            if -two_sum in N:
                r.add(tuple(sorted([p[i], p[j], -two_sum])))
    # complement of 2s negative
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            two_sum = n[i] + n[j]
            if -two_sum in P:
                r.add(tuple(sorted([n[i], n[j], -two_sum])))
    return [[x, y, z] for x, y, z in r]


def brute_force(nums: List[int]):
    ans = set()
    nums.sort()
    for ix, x in enumerate(nums):
        for iy, y in enumerate(nums):
            for iz, z in enumerate(nums):
                if x + y + z == 0:
                    if ix != iy and ix != iz and iy != iz:
                        a = sorted([x, y, z])
                        k, p, o = a
                        ans.add((k, p, o))
    return ans


three_sum(input)
# print(f"solution {three_sum(input)}")
expected = [
    [-4, 0, 4],
    [-4, 1, 3],
    [-3, -1, 4],
    [-3, 0, 3],
    [-3, 1, 2],
    [-2, -1, 3],
    [-2, 0, 2],
    [-1, -1, 2],
    [-1, 0, 1],
]


def test_three_sum():
    # assert len(expected) == len(three_sum(input))
    assert [[-1, -1, 2], [-1, 0, 1]] == complement(input)
