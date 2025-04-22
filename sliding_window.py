# Longest Substring Without Repeating Characters
# input = "abcabcbb"
# expected = 3
input = "aab"
expected = 2

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0
#         sub_string = []
#         for char in s:
#             if char not in sub_string:
#                 sub_string.append(char)
#                 max_len = max(max_len, len(sub_string))
#             else:
#                 idx = sub_string.index(char)
#                 sub_string = sub_string[idx+1:]
#                 sub_string.append(char)
#         if len(sub_string) > max_len:
#             max_len = len(sub_string)
#         return max_len
# a a b
#   r


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s)==1:
#             return 1
#         d={}
#         left,r = 0,0
#         maxLen = 0
#         while(r < len(s)):
#             if s[r] in d:
#                 left = max(left,d[s[r]]+1)
#             length = r - left +1
#             maxLen = max(maxLen,length)
#             d[s[r]]=r
#             r+=1
#         return maxLen
    
# x a b a c d a e
# 0 1 2 3
# l l   r

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        map = {}
        left = 0
        max_l = 0
        for right, c in enumerate(s):
            if c not in map:
                map[c] = right
            else:
                print(f'we found char {c} in map')
                left = max(map[c] + 1, left)
                map[c] = right
                print(f'setting left to {left}')
                length = right - left + 1
                print(f'len is {length} > {right} - {left} + 1')
                max_l = max(max_l, length)
        return max_l







actual = Solution().lengthOfLongestSubstring(input)
assert expected == actual, f"expected {expected} but got {actual}"
