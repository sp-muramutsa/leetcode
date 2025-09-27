class Solution:
    def numSquares(self, n: int) -> int:
        # Create a dp array
        # Each index represents minimum number of sq to add up to it
        # Iterate over the array
        # Find from the back the minimum number to add to it
        dp = [n] * (n+1)
        dp[0] = 0

        for trg in range(1, n+1):
            for sq in range(1, trg+1):
                square = sq*sq
                if square > trg:
                    break
                dp[trg] = min(dp[trg], 1 + dp[trg-square])
        return dp[-1]
