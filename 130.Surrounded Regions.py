from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # start from any boarder Os, keep them, other wise return
    ROWS, COLS = len(board), len(board[0])
    res = [["X" for _ in range(COLS)] for _ in range(ROWS)]
    visited = set()

    def dfs(row, col):
        if (
            row < 0
            or row == ROWS
            or col < 0
            or col == COLS
            or board[row][col] == "X"
            or (row, col) in visited
        ):
            return

        visited.add((row, col))
        res[row][col] = "O"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for col in range(COLS):
        dfs(0, col)
        dfs(ROWS - 1, col)

    for row in range(ROWS):
        dfs(row, 0)
        dfs(row, COLS - 1)

    return res


tmp = solve(
    [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
)

print(tmp)
