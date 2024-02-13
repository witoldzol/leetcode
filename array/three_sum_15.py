# https://leetcode.com/problems/3sum/description/
# return all 3 digits that add up to 0, no duplicates, all digits should be diff from each other
from typing import List

input = [-1,0,1,2,-1,-4]
input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

# def three_sum(input: List[int]):
#     if len(input) < 3:
#         return []
#     s = sorted(input)
#     for i in range(len(s)):
#         if s[i] > 0: # if we start with positive, and we are sorted, then we know that 0 is impossible
#             break
#         if i > 0 and s[i] == s[i -1 ]: # no idea what's going on here
#             continue
#         low, high = 0, len(s) - 1
#         while low < high:
#             sum = s[low] + s[high]

def three_sum(input: List[int]):
    d = {}
    for ix, x in enumerate(input):
        d[x] = ix
    s = sorted(input)
    low = 0
    high = len(s) - 1
    results = []
    while low < high:
        sum = s[low] + s[high]
        if sum > 0:
            if -sum in d:
                results.append((s[low], s[high], -sum))
        elif sum > 0:
            if sum in d:
                results.append((s[low], s[high], sum))




print(f"solution {three_sum(input)}")
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

def test_three_sum():
    assert len(expected) == len(three_sum(input))

