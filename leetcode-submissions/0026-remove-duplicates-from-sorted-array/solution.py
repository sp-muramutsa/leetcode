from collections import defaultdict 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        Intuition: We use a fast and slow pointer iterating form left to right.
        We use the left pointer to reserve space for the next unique value
        We iterate while comparing and when we find that unique value, we put it in the position of the second value of the current unique values
        """
        length = len(nums)
        l, r = 0, 1
        current = nums[l]

        while r < length:
            if nums[r] != current:
                nums[l+1] = nums[r]
                current = nums[r]
                l += 1
            r += 1
        
        return l + 1
                
        
        
       
        
        

    


                
    
        
