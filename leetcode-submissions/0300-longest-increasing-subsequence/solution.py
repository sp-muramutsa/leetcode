class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create a dp of max sequence
        dp = [1] * len(nums)
        # Starting from the second last element
        for i in range(len(nums)-2, -1, -1):
            # Ierate from current index and update dp with max lenght if number is greater than current index value
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        # Return the max dp value
        return max(dp)
