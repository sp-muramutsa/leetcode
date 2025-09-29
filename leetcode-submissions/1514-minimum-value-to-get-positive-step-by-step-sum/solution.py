class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current_sum = 0
        lowest_sum = 0
        
        for numbers in nums:
            current_sum += numbers
            lowest_sum = min(current_sum, lowest_sum)
            
        ans = abs(lowest_sum) + 1
        return ans
