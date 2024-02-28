# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
import pudb
from collections import deque
# input = [3,9,20,None,None,15,7]
# expected = [[3],[20,9],[15,7]]
input = [1,2,3,4,None, None,5]
expected = [[1],[3,2],[4,5]]
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# test data
# l2 = TreeNode(15, None, None)
# r2 = TreeNode(7, None, None)
# r1 = TreeNode(20, l2, r2)
# l1 = TreeNode(9, None, None)
# root = TreeNode(3, l1, r1)

r2 = TreeNode(5, None, None)
l2 = TreeNode(4, None, None)
r1 = TreeNode(3, None , r2)
l1 = TreeNode(2, l2, None)
root = TreeNode(1, l1, r1)
# loooks like we need to capture in a group all the nodes that are of the same hight relative to root
def zigzag(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque()
    q.append([root])
    flip = 1
    temp = []
    # pu.db
    while len(q):
        nodes = q.popleft()
        # update results
        vals = [n.val for n in nodes]
        vals = vals[::flip]
        result.append(vals)
        # update queue
        for node in nodes:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        if temp:
            q.append(temp[:])
        temp = []
        flip *= -1
    return result

# print(zigzag(root))

def zig(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    ans = []
    queue = deque([root])
    flip = 1
    while queue:
        levelVal = []
        for _ in range(len(queue)):
            node = queue.popleft()
            levelVal.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(levelVal[::flip])
        flip *= -1
    return ans
print(zigzag(root))
print("=======")
print(zig(root))
