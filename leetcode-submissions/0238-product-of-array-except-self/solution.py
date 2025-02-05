class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_multiplier, right_multiplier = 1, 1

        n = len(nums)
        
        # left
        left = [0] * n
        left[0] = 1
        for i in range(1, n):
            left[i] = nums[i-1] * left_multiplier
            left_multiplier = left[i]
        
        # right
        right = [0] * n
        right[-1] = 1
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right_multiplier
            right_multiplier = right[i]
        
        # result
        for i in range(n):
            nums[i] = left[i] * right[i]
        
        return nums
