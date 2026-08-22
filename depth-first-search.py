from functools import lru_cache
from typing import List


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        # visit every cell
        board_tup = tuple(tuple(row) for row in board)
        for x in range(len(board)):
            for y in range(len(board[0])):
                res = Solution.dfs(board_tup, word, (x, y), {(x, y)}, 0)
                if res:
                    return res
        return False

    # this will be our recursive call
    @staticmethod
    def dfs(
        board: tuple[tuple[str]],
        word: str,
        start: tuple[int, int],
        visited: set[tuple[int, int]],
        current_index: int,
    ) -> bool:
        # base condition - check if expected letter matches
        x, y = start
        # print(f" starting dfs {x}, {y}, {current_index=}, {visited=}")
        if board[x][y] != word[current_index]:
            # print(f"{board[x][y]=} != {word[current_index]} -> FALSE")
            return False
        if board[x][y] == word[current_index] and current_index == len(word) - 1:
            # print(f"returning true {current_index=}, {x=}, {y=}")
            return True
        current_index += 1
        if current_index >= len(word):
            # print(f"{current_index=} >= {len(word)=} -> FALSE")
            return False
        # check all directions
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for xx, yy in DIRECTIONS:
            dx = x + xx
            dy = y + yy
            if (
                dx < len(board)
                and dx >= 0
                and dy < len(board[0])
                and dy >= 0
                and (dx, dy) not in visited
            ):
                up_res = Solution.dfs(
                    board, word, (dx, dy), visited | {(dx, dy)}, current_index
                )
                if up_res:
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
res = Solution.exist(board, word)
assert True is res

word = "ABCB"
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
res = Solution.exist(board, word)
assert False is res

board = [["a", "a"]]
word = "aaa"
res = Solution.exist(board, word)
assert False is res

board = [["a", "b"], ["c", "d"]]
word = "bacd"
res = Solution.exist(board, word)
assert True is res


board = [["a", "b"], ["c", "d"]]
word = "cdba"
assert True is res
