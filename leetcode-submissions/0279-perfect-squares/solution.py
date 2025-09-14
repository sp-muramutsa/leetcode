class Solution:
    def numSquares(self, n: int) -> int:

        sqrt_n = sqrt(n)
        ceil_sqrt_n = ceil(sqrt_n)

        # Base case: n is a perfect square
        if sqrt_n == ceil_sqrt_n:
            return 1

        # Enumerate all possible perfect squares
        perfect_squares = [x**2 for x in range(1, ceil_sqrt_n)]

        # Make a dp table
        dp = [float("inf")] * (n + 1)

        # Base cases: perfect squares
        for y in perfect_squares:
            dp[y] = 1

        for i in range(2, n + 1):

            if dp[i] == 1:
                continue

            # Loop through all perfect squares less than i
            for y in perfect_squares:
                if y > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - y])

        return dp[-1]

