class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1] * n

        for start in range(n):
            for end in range(start + 1, n):
                if nums[start] < nums[end]:
                    dp[end] = max(dp[end], dp[start] + 1)

        return max(dp)

