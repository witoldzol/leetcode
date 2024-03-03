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

# r2 = TreeNode(11, None, None)
# l2 = TreeNode(1, None, None)
# r1 = TreeNode(10, None , r2)
# l1 = TreeNode(2, l2, None)
# root = TreeNode(5, l1, r1)

from typing import Optional, List
prev = [None]
result = [True]

def is_valid(root: Optional[TreeNode], prev, result) -> bool:
    if prev[0] != None:
        print(f"{prev[0].val=}")
    if root is None:
        return
    is_valid(root.left, prev, result)
    if prev[0]:
        print(f"current value is {root.val}, and previous value is = {prev[0].val}")
    if prev[0] and root.val <= prev[0].val:
        result[0] = False
        return
    prev[0] = root
    is_valid(root.right, prev, result)

vprev = None
vresult = [True]

def v(root: Optional[TreeNode], vprev, vresult) -> bool:
    if vprev != None:
        print(f"{vprev.val=}")
    if not root:
        return True
    v(root.left, vprev, vresult)
    if vprev:
        print(f"current value is {root.val}, and vprevious value is = {vprev.val}")
    if vprev and root.val <= vprev.val:
        vresult[0] = False
        return
    vprev = root
    v(root.right, vprev, vresult)

is_valid(root, prev, result)
print("==================================================")
print("==================================================")
print("==================================================")
v(root, vprev, vresult)
print(f"{result[0]=}")
print(f"{vresult[0]=}")


# def v(root: Optional[TreeNode], prev, result) -> bool:

