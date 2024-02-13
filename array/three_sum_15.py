# https://leetcode.com/problems/3sum/description/
# return all 3 digits that add up to 0, no duplicates, all digits should be diff from each other
from typing import List

input = [-1,0,1,2,-1,-4]

def three_sum(input: List[int]):
    # brute force - get all permutations & count they all up
# non brute? calc diff ? - 
# first pass create hash map of values 
# second pass look at reminder, then check if we have reminder, if not, geet another value and check for reminder
# when going 0 to n, calc first diff, say 5 - 0 = -5, so we need reminder of -5, then next one is -8, so now need reminder of 3


