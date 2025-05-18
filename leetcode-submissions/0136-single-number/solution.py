class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        for key, item in hashmap.items():
            if item == 1:
                return key
        
