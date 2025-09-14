class Solution:
    def climbStairs(self, n: int) -> int:
        # Tabulation method
        # A dp array of number of steps
        # First and second indices are 0 and 1 respectively
        # Starting from the third index find the sum of ways by  adding the sum of ways from 1 step back and 2 steps back
        # Return the last index in the array
        dp = [0] * (n+1)
        dp[1], dp[0] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]


        return dp[-1]

