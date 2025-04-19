from typing import List

# board =  \
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]

def validate_square(board):
    for k in range(0,9,3):
        for i in range(0,9,3):
            s = set()
            for x in range(k,k+3):
                for y in range(i,i+3):
                    cell = board[x][y]
                    if cell == '.':
                        continue
                    if cell in s:
                        return False
                    else:
                        s.add(cell)
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for x in row:
                if x in s:
                    if x == '.':
                        continue
                    print(x, ' found in set ', s)
                    return False
                else:
                    s.add(x)
        # column
        for i in range(9):
            s = set()
            for row in board:
                if row[i] == '.':
                    continue
                if row[i] in s:
                    print('COLUMN: ' , i)
                    print(row[i], ' found in set ', s)
                    return False
                else:
                    s.add(row[i])
        res = validate_square(board)
        print('res', res)
        if not res:
            return False
        return True

print(Solution().isValidSudoku(board))
