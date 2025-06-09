class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        counter = Counter(nums)
        for key, value in counter.items():
            bucket[value].append(key)
        res = []
        print(bucket)
        for i in bucket[::-1]:
            if len(i) != 0:
                for j in i:
                    res.append(j)
                    if len(res) == k:
                        return res
