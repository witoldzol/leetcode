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

# print(f"solution is = {inorder(root)}")

def is_valid(root: Optional[TreeNode], prev: int = float('-inf')) -> bool:
    # in order traversal -> go to the bottom of LEFT, then CENTER, then RIGHT
    # with each step, value should be higher, if not, we have invalid tree
    if not root:
        return True
    # left
    if root.left:
        if not is_valid(root.left, root.val):
            return False
    # root
    if root.val <= prev:
        return False
    # right
    return is_valid(root.right, root.val)


print(f"is_valid == {is_valid(root)}")
