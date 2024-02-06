from typing import List

input = ["eat","tea","tan","ate","nat","bat"]
expected =  [["bat"],["nat","tan"],["ate","eat","tea"]]

def group_anagrams(strs: List[str]) -> List[List[str]]:
    grouped = []
    for x in strs:
        for y in strs:
            if x == y:
                continue
            if is_anagram(x,y):
                grouped.append([x,y]) # todo we have to check if we alerady have a group with that anagram


assert [[""]] == group_anagrams([""]) 

def is_anagram(first: str, second) -> bool:
    f_dict = {}
    for c in first:
        if c in f_dict:
            f_dict[c] += 1
        else:
            f_dict[c] = 1
    for c in second:
        if c in f_dict:
            f_dict[c] -= 1
            if f_dict[c] == 0:
                del f_dict[c]
        else:
            return False
    if len(f_dict) == 0:
        return True
    return False

assert True == is_anagram("bob", "bbo")
assert False == is_anagram("bob", "bboo")
assert True == is_anagram("", "")
