class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)

        def dfs(idx):
            if idx >= n:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            dp[idx] = cost[idx] + min(dfs(idx+1), dfs(idx+2))
            return dp[idx]

        return min(dfs(0), dfs(1))
