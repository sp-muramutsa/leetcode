class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashmap = {}
        pairs = 0
        for i in nums:
            y1 = k + i
            y2 = i - k
            if hashmap.get(y1, None) is not None:
                pairs += hashmap.get(y1)
            if hashmap.get(y2, None) is not None:
                pairs += hashmap.get(y2)
            hashmap[i] = hashmap.get(i, 0) + 1
        return pairs
