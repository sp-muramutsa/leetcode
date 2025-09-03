class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        longest = 0

        for end in range(n):
            for prev in range(end):
                if nums[end] > nums[prev]:
                    dp[end] = max(dp[end], dp[prev] + 1)
                else:
                    dp[end] = max(dp[end], 1)
            longest = max(longest, dp[end])

        return longest

