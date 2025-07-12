import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        i = 0
        n = len(nums)
        heap = []
        
        for i in range(n):      
            heapq.heappush(heap, nums[i])
            
            if len(heap) > k :
                heapq.heappop(heap)
        
        return heap[0]


