class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        empties = []

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    empties.append((r, c))
                else:
                    value = board[r][c]

                    rows[r].add(value)
                    cols[c].add(value)
                    box = (r // 3) * 3 + (c // 3)
                    boxes[box].add(value)

        n = len(empties)

        def backtrack(i):

            if i == n:
                return True

            row, col = empties[i]
            box = (row // 3) * 3 + (col // 3)

            for j in range(1, 10):

                digit = str(j)
                if digit in rows[row] or digit in cols[col] or digit in boxes[box]:
                    continue

                cols[col].add(digit)
                rows[row].add(digit)
                boxes[box].add(digit)
                board[row][col] = digit

                if backtrack(i + 1):
                    return True

                cols[col].remove(digit)
                rows[row].remove(digit)
                boxes[box].remove(digit)
                board[row][col] = "."

            return False

        backtrack(0)

