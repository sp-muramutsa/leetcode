class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 2]:
                nums.remove(nums[i])
            else:
                i += 1

        return len(nums)
        

        
