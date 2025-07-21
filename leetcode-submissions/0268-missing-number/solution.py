class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # O(n) Time and O(1) space
        n = len(nums)
        gaussian_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        return gaussian_sum - actual_sum
