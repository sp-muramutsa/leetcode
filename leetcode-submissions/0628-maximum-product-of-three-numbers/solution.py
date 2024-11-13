class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        x = sorted(nums)
        # Case 1: Product of the three largest numbers
        option1 = x[-1] * x[-2] * x[-3]
        # Case 2: Product of the two smallest numbers (most negative) and the largest number
        option2 = x[0] * x[1] * x[-1]
        # Return the maximum of these two cases
        return max(option1, option2)
