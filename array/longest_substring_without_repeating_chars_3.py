# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import pudb

def lengthOfLongestSubstring(s: str) -> int:
    max_len: int = 0
    temp = []
    for x in s:
        if x in temp:
            max_len = max(max_len, len(temp))
            index = temp.index(x)
            temp = temp[index+1:]
            temp.append(x)
        else:
            temp.append(x)
    max_len = max(max_len, len(temp))
    return max_len

input = "abcabcbb"
a = lengthOfLongestSubstring(input)
assert a == 3
input = "bbbbb"
a = lengthOfLongestSubstring(input)
assert a == 1
input = "pwwkew"
a = lengthOfLongestSubstring(input)
assert a == 3
input = "aab"
a = lengthOfLongestSubstring(input)
assert a == 2
input = "dvdf"
a = lengthOfLongestSubstring(input)
assert a == 3
