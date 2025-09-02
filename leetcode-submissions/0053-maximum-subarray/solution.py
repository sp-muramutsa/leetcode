class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # DP: O(n) time and constant space
        n = len(nums)
        curr_sum = nums[0]
        maxx = curr_sum

        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            maxx = max(maxx, curr_sum)

        return maxx

