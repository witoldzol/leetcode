from collections import deque

matching_parens = {}
matching_parens["{"] = "}"
matching_parens["["] = "]"
matching_parens["("] = ")"

left = "{(["
right = "}])"

def check_parens(input: str) -> bool:
    stack = deque()
    for c in input:
        if c in left:
            stack.append(c)
        elif c in right:
            popped = stack.pop()
            if matching_parens[popped] != c:
                return False
    if not len(stack):
        return True
    return False

valid_input = "{([])}"
assert True == check_parens(valid_input)
invalid_input = "{([])"
assert False == check_parens(invalid_input)
