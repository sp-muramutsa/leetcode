class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for column in range(9):
                if board[row][column] == ".":
                    continue
                if board[row][column] in seen:
                    return False
                seen.add(board[row][column])
        
        for column in range(9):
            seen = set()
            for row in range(9):
                if board[row][column] == ".":
                    continue
                if board[row][column] in seen:
                    return False
                seen.add(board[row][column])
            
        for box_row in range(0, 9, 3):
            for box_column in range(0, 9, 3):
                seen = set()
                for i in range(box_row, box_row + 3):
                    for j in range(box_column, box_column + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True
