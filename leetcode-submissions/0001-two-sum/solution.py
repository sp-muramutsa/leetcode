class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {} # number : index

        for index, number in enumerate(nums):
            complement = target - number
            if complement in hashmap:
                return [hashmap[complement], index]
            else:
                hashmap[number] = index    
        return 
               
