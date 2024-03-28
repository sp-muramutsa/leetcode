from collections import defaultdict 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        Intuition: We use a fast and slow pointer iterating form left to right.
        We use the left pointer to reserve space for the next unique value
        We iterate while comparing and when we find that unique value, we put it in the position of the second value of the current unique values
        """
        length = len(nums)
        l, r = 0, 1

        while r < length:
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        
        return l + 1
        

   
        
    


        
        
        
       
        
        

    


                
    
        
