class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(prev, nums[1])

        for i in range(2, n):
            best = max(curr, nums[i] + prev)

            prev, curr = curr, best

        return curr

