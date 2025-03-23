class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        val = len(nums)/2
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in hashmap:
            if hashmap[i] >  val:
                return i
        
