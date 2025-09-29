class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Create dp that stores 
        # Edge case both first and second keep keep their minn price
        # Starting from the third index choose the min sum from prevous and second previous index
        # Update the dp price
        # Return min of last 2 indices

        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])


        return min(dp[-1], dp[-2])
