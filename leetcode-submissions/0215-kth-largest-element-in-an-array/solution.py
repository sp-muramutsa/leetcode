import heapq
class Solution:
    def findKthLargest(self, nums, k) -> int:
        heap = []
        for number in nums:
            heapq.heappush(heap, number)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]



        
