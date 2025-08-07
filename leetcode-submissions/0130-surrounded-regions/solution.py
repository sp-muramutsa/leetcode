import itertools


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        left = [(row, 0) for row in range(m)]
        right = [(row, n - 1) for row in range(m)]
        up = [(0, col) for col in range(n)]
        down = [(m - 1, col) for col in range(n)]

        borders = list(itertools.chain(left, right, up, down))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            """
            Mark any O that has a connection to the boarder with a letter "A" so it will be spared
            """

            board[r][c] = "A"

            for dx, dy in directions:
                x, y = r + dx, c + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    dfs(x, y)

        # Run dfs and mark the cells to be spared
        for row, col in borders:
            if board[row][col] == "O":
                dfs(row, col)

        # Iterate over the board and "capture" and "spare" cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

