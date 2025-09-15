class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        # First row
        for i in range(1, ROWS):
            grid[i][0] += grid[i - 1][0]
        
        # First column
        for j in range(1, COLS):
            grid[0][j] += grid[0][j - 1]

        # Other cells
        for row in range(1, ROWS):
            for col in range(1, COLS):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        
     
        return grid[-1][-1]
                

