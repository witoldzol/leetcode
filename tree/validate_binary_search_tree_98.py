# https://leetcode.com/problems/validate-binary-search-tree/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

r2 = TreeNode(5, None, None)
l2 = TreeNode(4, None, None)
r1 = TreeNode(3, None , r2)
l1 = TreeNode(2, l2, None)
root = TreeNode(1, l1, r1)

from typing import Optional, List

def inorder(root: Optional[TreeNode], result: List[int] = None,  prev: TreeNode = None) -> int:
    # in order traversal -> go to the bottom of LEFT, then CENTER, then RIGHT
    # with each step, value should be higher, if not, we have invalid tree
    if not root:
        return True
    if not result:
        result = []
    if root.left:
        result = inorder(root.left, result)
    result.append(root.val)
    if root.right:
        result = inorder(root.right, result)
    return result
    
print(f"solution is = {inorder(root)}")

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         prev = float('-inf')
#         def inorder(node):
#             nonlocal prev
#             if not node:
#                 return True
#             if not (inorder(node.left) and prev < node.val):
#                 return False
#             prev = node.val
#             return inorder(node.right)
#         return inorder(root)
