class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        # Iterate from the first element and then multiply from the front
        pre = 1
        for i in range(1, len(nums)):
            pre *= nums[i-1]
            prefix[i] = pre
            
        su = 1
        for i in range(len(nums)-2, -1, -1):
            su *= nums[i+1]
            suffix[i] = su
            
        for i in range(len(suffix)):
            prefix[i] = prefix[i] * suffix[i]
            
        return prefix
