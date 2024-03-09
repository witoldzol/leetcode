def firstUniqChar_old(s: str) -> int:
    encountered = []
    repeated = []
    for c in s:
        if c in repeated:
            continue
        elif c in encountered:
            repeated.append(c)
        encountered.append(c)
    to_return = ""
    for c in encountered:
        if c not in repeated:
            to_return = c
            break
    print(f"{encountered=}")
    if not to_return:
        return -1
    for i, c in enumerate(s):
        if c == to_return:
            return i
    raise Exception("oh oh somehing went wrong")


def test_first_unique():
    assert 0 == firstUniqChar_old("leetcode")


def firstUniqChar(s: str) -> int:
    map = {}
    for c in s:
        map[c] = map.get(c, 0) + 1
    for i, c in enumerate(s):
        if map[c] == 1:
            return i
    return -1
