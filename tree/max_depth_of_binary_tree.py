from __future__ import annotations
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

class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:



