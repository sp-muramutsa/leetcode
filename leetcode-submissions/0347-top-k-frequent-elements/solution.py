class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        nums_list = [[] for i in range(len(nums) + 1)]
        for key, value in hashmap.items():
            nums_list[value].append(key)
        res = []
        for i in nums_list[::-1]:
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res
            
