class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Fill in first cell
        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # Fill in the the first row
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] if obstacleGrid[i][0] == 0 else 0

        # Fill in the first column
        for j in range(1, n):
            obstacleGrid[0][j] = obstacleGrid[0][j - 1] if obstacleGrid[0][j] == 0 else 0

        # Fill in the rest of the cells
        for row in range(1, m):
            for col in range(1, n):   
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]

        return obstacleGrid[-1][-1] 
