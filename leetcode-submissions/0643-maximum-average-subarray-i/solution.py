class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = 0
        
        i = 0
        while i in range(k):
            current += nums[i]
            i += 1
            
        average = current / k
        
        left = 0
        right = k
        
        ans = average
        
        while right < len(nums):
            current -= nums[left]
            current += nums[right]
            
            average = current / k
            
            left += 1
            right += 1
            
            ans = max(ans, average)
            
        return ans
            
            
