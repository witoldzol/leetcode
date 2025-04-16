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

def validate_square(n,m,j,k):
    s = set()
    for i in range(n,m):
        for k in range(j,k):
            cell = board[i][k]
            if cell == '.':
                continue
            if cell in s:
                return False
            else:
                s.add(cell)
    return True

def validate(board):
    # row
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
    res = all(validate_square(0,3,0,3)
    return True

print(validate(board))
