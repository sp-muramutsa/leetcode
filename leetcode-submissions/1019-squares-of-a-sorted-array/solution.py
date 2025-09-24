class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        new_list = [0] * len(nums)
        
        counter = len(new_list) - 1
        
        while i <= j :
            if ((nums[j] * nums[j]) > (nums[i] *nums[i])):
                new_list[counter] = (nums[j] * nums[j])
                j -= 1
                
            else:
                new_list[counter] = (nums[i] * nums[i])
                i += 1
            counter -= 1
            
        return new_list
