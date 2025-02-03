from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(nums):
            hashmap[number] = index
        
        n = len(nums)
        print(hashmap)

        for i in range(n):
            diff = target - nums[i]

            if diff in hashmap and i != hashmap[diff]:
                return [i, hashmap[diff]]
                
            

        
