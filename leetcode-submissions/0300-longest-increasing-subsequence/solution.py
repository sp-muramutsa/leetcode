class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = float("-inf")

        for i in range(len(nums)-2, -1, -1):
            ans = 1
            for j in range(i+1, len(dp)):
                if nums[j] > nums[i]:
                    ans = max(ans, (1+dp[j]))
            dp[i] = ans
            res = max(res, ans)
            print(res)

        if res == float("-inf"):
            return 1

        return res
