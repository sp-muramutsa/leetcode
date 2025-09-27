class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Using Tabulation or Bottom up
        # Create a dp of length 11
        # Edge case 0
        # Starting from 1 Find the remainder and take the minimum
        # Reach the end and return the last index value if it not infinity

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i-j] + 1)

        print(dp)

        if dp[-1] == float("inf"):
            return -1

        return dp[-1]
