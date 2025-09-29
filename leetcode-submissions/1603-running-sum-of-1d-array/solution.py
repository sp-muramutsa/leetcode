class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        running_sum = nums[0]
        
        for counter in range(1, len(nums)):
            running_sum += nums[counter]
            prefix_sum.append(running_sum)
            
        return prefix_sum
        
