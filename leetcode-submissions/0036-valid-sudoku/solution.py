class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):

            # Horizontal
            horizontal = set()
            vertical = set()
            for j in range(9):

                if board[i][j] != ".":
                    if board[i][j] in horizontal:
                        return False
                    horizontal.add(board[i][j])

                # Vertical
                if board[j][i] != ".":
                    if board[j][i] in vertical:
                        return False
                    vertical.add(board[j][i])

        # 3x3
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                box = set()
                for a in range(row, row + 3):
                    for b in range(col, col + 3):

                        if board[a][b] != ".":
                            if board[a][b] in box:

                                return False
                            box.add(board[a][b])
        return True

