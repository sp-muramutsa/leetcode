class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        
        current_number_of_zeroes = 0
        ans = 0        
        
        while right < len(nums):
            if nums[right] == 0:
                current_number_of_zeroes += 1
                
            if current_number_of_zeroes > k:
                while nums[left] != 0:
                    left += 1
                left += 1
                current_number_of_zeroes -= 1
                
            current_length = (right - left) + 1
            ans = max(ans, current_length)
            right += 1
            
        return ans
        
