class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Tabulation: Can we make up this target sum using i first elements ?

        total = sum(nums)

        if total % 2 == 1:
            return False

        n = len(nums)
        target_sum = total // 2

        dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for curr_sum in range(target_sum + 1):

                sum_we_need = curr_sum - nums[i - 1]
                if abs(sum_we_need) + 1 > target_sum:
                    continue

                choose = dp[i - 1][sum_we_need]
                not_choose = dp[i - 1][curr_sum]
                dp[i][curr_sum] = choose or not_choose

        for x in range(n + 1):
            if dp[x][-1]:
                return True

        return False

