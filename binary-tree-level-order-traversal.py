from __future__ import annotations
from collections import deque
from typing import Any

values = [3, 9, 20, None, None, 15, 7]


class Node:
    def __init__(
        self, value: int, left: Node | None = None, right: Node | None = None
    ) -> None:
        self.value: int = value
        self.left = left
        self.right = right


#     root
#   l     r
# ll rr rl rr
def create_tree(values: list[int]) -> Node | None:
    root = None
    queue = deque()
    i = 0
    if values:
        root = Node(values[i])
        queue.append(root)
        i += 1
    while queue:
        current = queue.popleft()
        # print(current.value)
        # add left
        if i < len(values):
            left = Node(values[i])
            current.left = left
            queue.append(left)
            i += 1
        # add right
        if i < len(values):
            right = Node(values[i])
            current.right = right
            queue.append(right)
            i += 1
    return root


root = create_tree(values)


#   a
#  b  b
# c c _ c
def bfs(root: Node | None) -> None:
    if not root:
        return
    q = deque()
    if root:
        q.append(root)
    i = 0
    while q:
        tmp = []
        for n in q:
            print(n.value)
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)
        print(f"end of level: {i}")
        i += 1
        while q:
            q.popleft()
        for n in tmp:
            q.append(n)


bfs(root)
