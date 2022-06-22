def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    LOCATION = set()

    def dfs(r, c, i):

        if i == len(word):
            return True

        if (
            r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or board[r][c] != word[i]
            or (r, c) in LOCATION
        ):
            return False

        LOCATION.add((r, c))

        result = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )

        LOCATION.remove((r, c))

        return result

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(exist(board, word))
