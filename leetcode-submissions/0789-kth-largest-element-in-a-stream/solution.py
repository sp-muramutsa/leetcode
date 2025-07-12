import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        # Initialize a heap of size k
        # K-th largest element will be at the root
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        
        # If the new value is greater than the k-th largest element(root), push it on the heap. 

        # Edge case of when we start with fewer elements than k
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappush(self.min_heap, val)

        # Make sure the heap doesn't exceed size k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return the k-th largest element i.e. the root
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

