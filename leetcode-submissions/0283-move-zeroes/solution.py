class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time: O(n) 
        Space: O(n)
        Intuition: Move left to right pushing non-zero elements to the start. Pushing zeros to the end wasn't quite working!
        """

        i = 0
        n = len(nums)
        j = 1

        if n <= 1:
            return 


        while j < n:
            if nums[i] != 0:
                i += 1
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
           
            j += 1
        

        
             
