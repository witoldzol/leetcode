# Longest Substring Without Repeating Characters
input = "abcabcbb"
expected = 3
input = "aab"
expected = 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_string = []
        for char in s:
            if char not in sub_string:
                sub_string.append(char)
                max_len = max(max_len, len(sub_string))
            else:
                idx = sub_string.index(char)
                sub_string = sub_string[idx+1:]
                sub_string.append(char)
        if len(sub_string) > max_len:
            max_len = len(sub_string)
        return max_len

actual = Solution().lengthOfLongestSubstring(input)
assert expected == actual, f"expected {expected} but got {actual}"
