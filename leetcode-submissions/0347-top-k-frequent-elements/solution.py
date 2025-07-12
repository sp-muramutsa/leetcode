class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        heap = []
        for element, count in counter.items():
            heapq.heappush(heap, (count, element))
            if len(heap) > k:
                heapq.heappop(heap)

        return [element for count, element in heap]

