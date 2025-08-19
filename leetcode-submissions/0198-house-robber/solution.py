class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[0], nums[1])
        res = curr

        for i in range(2, n):
            res = max(nums[i] + prev, curr)
            prev, curr = curr, res

        return res

