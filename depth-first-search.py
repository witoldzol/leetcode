from typing import List


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        def dfs(
            start: tuple[int, int],
            current_index: int,
        ) -> bool:
            if current_index == len(word):
                return True
            x, y = start
            if board[x][y] != word[current_index]:
                return False
            if board[x][y] == word[current_index] and current_index == len(word) - 1:
                return True
            current_index += 1
            if current_index >= len(word):
                return False
            # check all directions
            DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
            temp = board[x][y]
            board[x][y] = "#"
            for xx, yy in DIRECTIONS:
                dx = x + xx
                dy = y + yy
                if dx < len(board) and dx >= 0 and dy < len(board[0]) and dy >= 0:
                    up_res = dfs(
                        (dx, dy),
                        current_index,
                    )
                    if up_res:
                        return True
            board[x][y] = temp
            return False

        # visit every cell
        for x in range(len(board)):
            for y in range(len(board[0])):
                res = dfs((x, y), 0)
                if res:
                    return res
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
