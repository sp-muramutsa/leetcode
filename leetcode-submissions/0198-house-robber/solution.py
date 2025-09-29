class Solution:
    def rob(self, nums: List[int]) -> int:
        # Create a dp of that store maximum money at position index
        # Starting from 3rd last position update the index
        # Skip adjacent index and update the sum of money with max 
        # Return max money from dp array

        dp = [n for n in nums]

        for i in range(len(nums)-3, -1, -1):
            n = dp[i]
            for j in range(i+2, len(nums)):
                n = max(n, (dp[i] + dp[j]))
            dp[i] = n

        return max(dp)
