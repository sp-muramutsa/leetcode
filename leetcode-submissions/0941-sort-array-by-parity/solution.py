class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(length - i -1):
                if nums[j] % 2 != 0:
                    nums[j], nums[j + 1] = nums[j +1], nums[j]
        return nums
    
        
