class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        longest = 0
        i, length = 0, len(nums)
        
        while i < length:
            if nums[i] - 1 not in hashset: # start of sequence
                sequence = 1
                number = nums[i]
                while number + 1 in hashset:
                    sequence += 1
                    number += 1
                longest = max(longest, sequence)
            i += 1
    
        return longest
            


            



        
            


        
        

        
        
            


        
        

        
