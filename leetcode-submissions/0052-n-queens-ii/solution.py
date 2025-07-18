class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()  # row + col
        neg_diag = set()  # row - col

        solution = 0

        def backtrack(row):

            if row == n:
                nonlocal solution
                solution += 1
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                backtrack(row + 1)

                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        backtrack(0)
        return solution

