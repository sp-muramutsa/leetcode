from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1: Map
        counter = Counter(nums)

        heap = []
        
        for value, frequency in counter.items():
            heapq.heappush(heap, (frequency, value))

            if len(heap) > k:
                heapq.heappop(heap)
               
        
        return [pair[1] for pair in heap]
