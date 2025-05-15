class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we create a hashmap that counts the number of times a number repeats itself
        #we create another hashmap that keeps a list of times numbers were repeated
        #we sort the hashmap 
        #we return the values

        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        l = [[] for i in range(len(nums)+1)]
        for i, n in hashmap.items():
            l[n].append(i)
        res = []
        for i in l[::-1]:
            for j in i:
                if len(res) < k:
                    res.append(j)
                else:
                    break
        return res
        
