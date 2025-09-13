class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Optimized Knapsack
        n = len(nums)

        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True

        for i in range(n):
            for curr_sum in range(half, nums[i] - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - nums[i]]

        return dp[-1]

