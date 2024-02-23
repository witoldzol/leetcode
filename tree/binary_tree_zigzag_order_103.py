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

# test data
l2 = TreeNode(15, None, None)
r2 = TreeNode(7, None, None)
r1 = TreeNode(20, l2, r2)
l1 = TreeNode(9, None, None)
root = TreeNode(3, l1,l2)

def zigzag(root: TreeNode) -> List[List[int]]:
    # bfs
    result = []
    from collections import deque
    q = deque()
    q.append(root)
    direction = 'left'
    temp = []
    while len(q):
        node = q.popleft()
        print(node.val)
        result.append(temp)
        if direction == 'left':
            if node.left:
                q.append(node.left)
                temp.append(node.left.val)
            if node.right:
                q.append(node.right)
                temp.append(node.right.val)
            result.append(temp)
            if direction == 'left':
                direction = 'right'
            else:
                direction = 'left'
        else:
            if node.right:
                q.append(node.right)
                temp.append(node.right.val)
            if node.left:
                q.append(node.left)
                temp.append(node.left.val)
            if direction == 'left':
                direction = 'right'
            else:
                direction = 'left'


zigzag(root)
