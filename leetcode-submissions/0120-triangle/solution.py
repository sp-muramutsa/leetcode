class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Using tabulation method
        # Create last array to kepp track of the minimum paths
        # Make your way up keeping and return the first element of the dp array
        dp = [0] * (len(triangle)+1)

        for i in triangle[::-1]:
            for j, n in enumerate(i):
                dp[j] = n + min(dp[j], dp[j+1])
        return dp[0]
