class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2
        dp = [[False] * (half + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for curr_sum in range(1, half + 1):

                # Choose
                complement = curr_sum - nums[i - 1]
                if complement >= 0 and dp[i - 1][complement]:
                    dp[i][curr_sum] = True

                # Not choose
                if dp[i - 1][curr_sum]:
                    dp[i][curr_sum] = True

                if curr_sum == half and dp[i][curr_sum]:
                    return True

        return False

