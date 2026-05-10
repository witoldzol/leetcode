from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


tree = [4, 2, 7, 1, 3, 6, 9]


def build_tree(input: list[int]) -> TreeNode | None:
    if not input:
        return None
    q = deque()
    root = TreeNode(input[0])
    q.append(root)
    i = 1
    # import pudb
    #
    # pu.db
    while q and i < len(input):
        node = q.popleft()
        left = TreeNode(input[i])
        q.append(left)
        node.left = left

        i += 1
        if i >= len(input):
            break
        right = TreeNode(input[i])
        q.append(right)
        node.right = right
        i += 1
    return root


root = build_tree(tree)
Solution().invertTree(root)
# print(root.left.left.val)
