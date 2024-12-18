class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [nums[0]]
        if not nums:
            return False
        answ = []
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        hashmap = sorted(hashmap.items(), key= lambda x: x[1], reverse=True)
        answ = []
        for i in range(k):
            answ.append(hashmap[i][0])
        return answ
       
                
