# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_false_tree():
    r2 = TreeNode(5, None, None)
    l2 = TreeNode(4, None, None)
    r1 = TreeNode(3, None , r2)
    l1 = TreeNode(2, l2, None)
    return TreeNode(1, l1, r1)

def get_true_tree():
    r2 = TreeNode(11, None, None)
    l2 = TreeNode(1, None, None)
    r1 = TreeNode(10, None , r2)
    l1 = TreeNode(2, l2, None)
    return TreeNode(5, l1, r1)

def vv(root: Optional[TreeNode]) -> bool:
    p = float('-inf')
    result = True
    def v(root: Optional[TreeNode]) -> bool:
        nonlocal p
        nonlocal result
        if not root:
            return True
        v(root.left)
        if p > root.val:
            result = False
        p = root.val
        v(root.right)
        return result
    return v(root)

print(f"result = {vv(get_true_tree())}")
print(f"result = {vv(get_false_tree())}")
