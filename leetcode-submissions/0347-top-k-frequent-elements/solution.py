class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        l = [[] for i in range(len(nums) +  1)]
        for key, value in hashmap.items():
            l[value].append(key)
        ans = []
        for i in range(len(l)-1, -1, -1):
            for j in l[i]:
                ans.append(j)
                if len(ans) == k:
                    break
            if len(ans) == k:
                break
        return ans

