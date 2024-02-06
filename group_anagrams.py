from typing import List

input = ["eat","tea","tan","ate","nat","bat"]
expected =  [["bat"],["nat","tan"],["ate","eat","tea"]]

def group_anagrams(strs: List[str]) -> List[List[str]]:
    grouped = []
    for x in strs:
        found = False
        for g in grouped:
            if is_anagram(x,g[0]):
                g.extend([x])
                found = True
        if not found:
            grouped.append([x])
    return grouped

def test_group_anagrams():
    assert [[""]] == group_anagrams([""]) 
    # assert expected == group_anagrams(input) 
    print(group_anagrams(input) )


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
