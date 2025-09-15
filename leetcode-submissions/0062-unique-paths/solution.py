class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]
        directions = [(0, 1), (1, 0)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    dp[nr][nc] += dp[row][col]

        return dp[-1][-1]

