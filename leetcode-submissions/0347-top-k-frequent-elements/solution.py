class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we create a hashmap
        hashmap = {}
        #we get the counts for number 0(n) Time 
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        #create a list with index as number of occurences
        res = [[] for i in range(len(nums)+1)]
        for key, value in hashmap.items():
            res[value].append(key)
        ans = []
        for i in res[::-1]:
            for j in i:
                ans.append(j)
                if len(ans) == k:
                    return ans
