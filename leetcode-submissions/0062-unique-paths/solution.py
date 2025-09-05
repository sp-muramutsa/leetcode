class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Using iterative method bottom-up we make our way to the destination
        # We can only move in twoo ways which signals dp, also we are counting ways to reach the goal
        # Create the Matrix with 0 inputs
        dp = [[0 for i in range(n)] for j in range(m)]
        # As the first row and first column only have one way to get rached on we mark them with 1
        for i in range(n):
            dp[0][i] = 1

        for j in range(m):
            dp[j][0] = 1
        # Iterate over the cells 
        # The other cells you find the number of ways to reach them by adding the upper cell and left cell paths
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the final cell
        return dp[-1][-1]

        #Time comlexity O(m*n)
        # Space complexity O(m*n)
