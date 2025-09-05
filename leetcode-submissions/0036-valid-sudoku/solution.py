class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create empty sets of rows and columns
        # Create set for 3x3 grid
        # Iterate over the elements in the grid
        # If the element is already in any of the position set return False
        # Add it to the sets
        # Return True

        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        sub_grid = []
        for i in range(3):
            n = []
            for j in range(3):
                n.append(set())
            sub_grid.append(n)


        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in sub_grid[i//3][j//3]:
                    return False

                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                sub_grid[i//3][j//3].add(board[i][j])

        return True
                
