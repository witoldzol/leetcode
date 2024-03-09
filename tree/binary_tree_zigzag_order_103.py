# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


r2 = TreeNode(5, None, None)
l2 = TreeNode(4, None, None)
r1 = TreeNode(3, None, r2)
l1 = TreeNode(2, l2, None)
root = TreeNode(1, l1, r1)


def zigzag(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque()
    q.append([root])
    order = 1  # 1 = left to right, -1 = right to left
    while q:
        temp = []
        nodes = q.popleft()
        values = [n.val for n in nodes][::order]  # reverse order if need be
        result.append(values)
        for node in nodes:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        if temp:
            q.append(temp)
        temp = []
        order *= -1
    return result


print(zigzag(root))
