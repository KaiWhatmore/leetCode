import collections


def isValidSudoku(board):

    blank = "."
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for c in range(9):
        for r in range(9):
            if (
                board[r][c] in rows[r]
                or board[r][c] in columns[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            if board[r][c] != blank:
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

    return True
