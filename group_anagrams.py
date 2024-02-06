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
