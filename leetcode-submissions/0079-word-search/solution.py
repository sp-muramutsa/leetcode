class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        word_len = len(word)

        starts = [
            (row, col)
            for row in range(ROWS)
            for col in range(COLS)
            if board[row][col] == word[0]
        ]

        def backtrack(cell, ROWS, COLS, word_idx):
            row, col = cell

            if board[row][col] != word[word_idx]:
                return False

            if word_idx == word_len - 1:
                return True

            char = board[row][col]
            board[row][col] = "#"

            for dx, dy in movements:
                x = row + dx
                y = col + dy

                if 0 <= x < ROWS and 0 <= y < COLS:
                    if backtrack((x, y), ROWS, COLS, word_idx + 1):
                        return True

            board[row][col] = char
            return False

        for start in starts:
            if backtrack(start, ROWS, COLS, 0):
                return True

        return False

