class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < (2 * k) + 1:
            return [-1] * len(nums)
        
        prefix_sum = [nums[0]]
        running_sum = nums[0]
        
        for i in range(1,len(nums)):
            running_sum += nums[i]
            prefix_sum.append(running_sum)
            
        avg_array = [-1] * len(nums)
        
        left = 0
        middle = k
        right = k + k
        
        while right < len(nums):
            amount = (2 * k) + 1
            total_sum = (prefix_sum[right] - prefix_sum[left]) + nums[left]
            avg = total_sum // amount
            
            avg_array[middle] = avg
            
            left += 1
            middle += 1
            right += 1
            
        return avg_array
        
