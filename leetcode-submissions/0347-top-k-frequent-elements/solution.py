class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for key, items in counter.items():
            bucket[items].append(key)
        bucket = bucket[::-1]
        res = []
        for i in bucket:
            if len(res) == k:
                return res
            else:
                for j in i:
                    res.append(j)
