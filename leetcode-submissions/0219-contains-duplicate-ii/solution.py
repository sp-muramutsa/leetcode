class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        """
        Time O(n)
        Space O(n)
        """
  
        nums_to_i = {} 
        length = len(nums)

        for i in range(length):
            if nums[i] in nums_to_i:
               if abs(i - nums_to_i[nums[i]]) <= k:
                    return True
            nums_to_i[nums[i]] = i
      
        return False
        
        
       

        
