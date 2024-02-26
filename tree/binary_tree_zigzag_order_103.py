# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
import pudb
from collections import deque
input = [3,9,20,None,None,15,7]
expected = [[3],[20,9],[15,7]]

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# test data
l2 = TreeNode(15, None, None)
r2 = TreeNode(7, None, None)
r1 = TreeNode(20, l2, r2)
l1 = TreeNode(9, None, None)
root = TreeNode(3, l1, r1)

def zigzag(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque()
    q.append(root)
    result.append([root.val])
    direction = 'left'
    temp = []
    while len(q):
        node = q.popleft()
        print(node.val)
        if direction == 'right':
            if node.left:
                q.append(node.left)
                temp.append(node.left.val)
            if node.right:
                q.append(node.right)
                temp.append(node.right.val)
            direction = 'left'
        else:
            if node.right:
                q.append(node.right)
                temp.append(node.right.val)
            if node.left:
                q.append(node.left)
                temp.append(node.left.val)
            direction = 'right'
        if temp:
            result.append(temp[:])
        temp = []
    print(f"result {result}")
    return result


zigzag(root)
