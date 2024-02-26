# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
import pudb
from collections import deque
# input = [3,9,20,None,None,15,7]
# expected = [[3],[20,9],[15,7]]
input = [1,2,3,4,null,null,5]
expected = [[1],[3,2],[4,5]]
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

# def zigzag(root: TreeNode) -> List[List[int]]:
#     if not root:
#         return []
#     result = []
#     q = deque()
#     q.append(root)
#     result.append([root.val])
#     direction = 'left'
#     temp = []
#     while len(q):
#         node = q.popleft()
#         print(node.val)
#         if direction == 'right':
#             if node.left:
#                 q.append(node.left)
#                 temp.append(node.left.val)
#             if node.right:
#                 q.append(node.right)
#                 temp.append(node.right.val)
#             direction = 'left'
#         else:
#             if node.right:
#                 q.append(node.right)
#                 temp.append(node.right.val)
#             if node.left:
#                 q.append(node.left)
#                 temp.append(node.left.val)
#             direction = 'right'
#         if temp:
#             result.append(temp[:])
#         temp = []
#     print(f"result {result}")
#     return result

def zigzag(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque()
    q.append([root])
    direction = 'left'
    temp = []
    # pu.db
    while len(q):
        nodes = q.popleft()
        vals = [n.val for n in nodes]
        result.append(vals)
        for node in nodes:
            if direction == 'right':
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            else:
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            if temp:
                q.append(temp[:])
            temp = []
        if direction == 'left':
            direction = 'right'
        else:
            direction = 'left'
    return result

print(zigzag(root))
