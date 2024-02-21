# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
input = [3,9,20,null,null,15,7]
expected = [[3],[20,9],[15,7]]

from typing import List

def zig(tree: List[int]) -> List[List[int]]:
    result = []
    if len(tree) < 2:
        return [tree]
    root = tree.pop(0)
    result.append([root])
    direction = 'left'
    count = 0
    temp = []
    for x in tree:
        if count == 2:
            temp.append(result)
            temp = []
        if direction == 'left':
            temp.append
        else:
            if count == 0:
                temp = [None, x]
            else:
                temp[0] = x
        count += 1





assert zig(input) == expected
