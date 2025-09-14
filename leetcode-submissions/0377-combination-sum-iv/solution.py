class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0] * (target + 1)
        dp[0] = 1

        for curr_sum in range(1, target + 1):
            for number in nums:
                if number > curr_sum:
                    continue
                dp[curr_sum] += dp[curr_sum - number]

        return dp[-1]

