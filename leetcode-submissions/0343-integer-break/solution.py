class Solution:
    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)

        for i in range(4):
            dp[i] = i

        for j in range(4, n + 1):
            dp[j] = j
            for k in range(j):
                dp[j] = max(dp[j], k * dp[j - k])

        return dp[-1]

