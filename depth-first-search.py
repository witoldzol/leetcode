from typing import List


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        # visit every cell
        for x in range(len(board)):
            for y in range(len(board[0])):
                # print(f"checking {x},{y}")
                res = Solution.dfs(board, word, (x, y), {(x, y)}, 0)
                if res:
                    return res
        return False

    # this will be our recursive call
    @staticmethod
    def dfs(
        board: list[list[str]],
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
        # check up
        dx = x - 1
        dy = y
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
        # check down
        dx = x + 1
        dy = y
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

        # check left
        dx = x
        dy = y - 1
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
        # check right
        dx = x
        dy = y + 1
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
        # default passthrough
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
