class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum, max_sum = 0, float('-inf')
        length = len(nums)
        
        for i in range(length):
            curr_sum = max(nums[i], curr_sum + nums[i])       
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

        
