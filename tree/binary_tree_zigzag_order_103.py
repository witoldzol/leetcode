# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
import pudb
input = [3,9,20,None,None,15,7]
expected = [[3],[20,9],[15,7]]

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig(tree: List[int]) -> List[List[int]]:
    # pu.db
    result = []
    if len(tree) < 2:
        return [tree]
    root = tree.pop(0)
    result.append([root])
    direction = 'right'
    count = 0
    temp = []
    for x in tree:
        if x == None:
            continue
        # flush after every 2 insertions
        if count == 2:
            result.append(temp)
            temp = []
            count = 0
            if direction == 'left':
                direction = 'right'
            else: 
                direction = 'left'
        # insertion 
        if direction == 'left':
            temp.append(x)
        else:
            if count == 0:
                temp = [None, x]
            else:
                temp[0] = x
        count += 1
    if count == 2:
        result.append(temp)
    return result

print(zig(input) )
print(f"exptected = {expected}")
