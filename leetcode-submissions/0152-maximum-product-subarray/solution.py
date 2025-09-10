class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minimum = maximum = max_product = nums[0]
        n = len(nums)

        for i in range(1, n):
            number = nums[i]
            local_max = max(number * minimum, number, number * maximum)
            minimum = min(number * minimum, number, number * maximum)
            maximum = local_max
            max_product = max(max_product, local_max)

        return max_product

