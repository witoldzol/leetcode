from __future__ import annotations
from collections import deque
from typing import Optional
from dataclasses import dataclass

input = [3,9,20,None,None,15,7]
out = 3

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

@dataclass
class Node:
    left: Node
    right: Node
    val: int = 0
ll = Node(None, None)
dd = Node(None, None)
l = Node(ll,dd,9)
rl = Node(None, None, 15)
rr = Node(None, None, 7)
r = Node(rl, rr, 20)
root = Node(l,r,3)

class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        depth = 0
        queue = deque()
        queue.append([root])
        while queue:
            level = queue.popleft()
            depth += 1
            next = []
            for node in level:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if next:
                queue.append(next)
        return depth

print(f"solution: {Solution().maxDepth(root)}")
