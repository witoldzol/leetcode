# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional, List
# import pudb; pudb.set_trace()
# import pubd
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

def test_is_valid():
    global prev
    global result
    is_valid(get_true_tree(), prev, result)
    assert True == result[0]
    prev = [None]
    result = [True]
    is_valid(get_false_tree(), prev, result)
    assert False == result[0]
    print("================================================================================")
    print("================================================================================")
    print("================================================================================")

def v(root: Optional[TreeNode], prev: int = float('-inf')) -> bool:
    # pu.db
    if not root:
        return None
    v(root.left, root.val)
    if prev and root.val < prev:
        return False
    print(f"visiting node = {root.val}, previous node = {prev}")
    r = v(root.right, root.val)
    if r == False:
        return False
    return True

print(f"result = {v(get_true_tree())}")
