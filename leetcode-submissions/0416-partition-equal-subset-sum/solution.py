class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        total = sum(nums)

        if total % 2 == 1:
            return False

        half = total // 2
        memo = {}

        
        def backtrack(i, remaining_sum):

            if (i, remaining_sum) in memo:
                return memo[(i, remaining_sum)]

            if remaining_sum == 0:
                return True

            if i == n:
                return False

            memo[(i, remaining_sum)] = False
            if backtrack(i + 1, remaining_sum - nums[i]):
                memo[(i, remaining_sum)] = True
                return memo[(i, remaining_sum)]
            elif backtrack(i + 1, remaining_sum):
                memo[(i, remaining_sum)] = True
                return memo[(i, remaining_sum)]
            
            return memo[(i, remaining_sum)]

        return backtrack(0, half)

