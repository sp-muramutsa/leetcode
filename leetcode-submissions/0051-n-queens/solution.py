class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()
        pos_diag = set()  # row + col
        neg_diag = set()  # row - col

        solution = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):

            if row == n:
                answer = ["".join(row) for row in board]
                solution.append(answer)
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        backtrack(0)
        return solution

