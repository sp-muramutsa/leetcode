class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minn = maxx = max_product = nums[0]
        n = len(nums)

        for i in range(1, n):
            x = nums[i]
            prev_max, prev_min = maxx, minn
            maxx = max(x, prev_max * x, prev_min * x)
            minn = min(x, prev_max * x, prev_min * x)
            max_product = max(maxx, max_product)

        return max_product

