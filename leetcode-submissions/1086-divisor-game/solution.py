class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = {}
        dp[1] = False
        dp[2] = True

        for i in range(3, n + 1):
            if i % 2 != 0:   # case for odd i
                dp[i] = not dp[i - 1]
            else:            # case for even i
                dp[i] = not dp[i - 1] or not dp[i - 2]

        return dp[n]
