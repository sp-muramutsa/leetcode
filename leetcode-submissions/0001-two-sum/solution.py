class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        """

        length = len(nums)
        hashmap = {}
        
        
        for i in  range(length):
            hashmap[target - nums[i]] = i 
        print(hashmap)
        
        for key, value in enumerate(nums):
            if value in hashmap and hashmap[value] != key:
                return [hashmap[value], key]




        
