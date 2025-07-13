class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min hea
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        
        # Add to the small heap
        heapq.heappush(self.small, -num)
        
        # Balance both heaps
        largest_left = heapq.heappop(self.small) 
        heapq.heappush(self.large, -largest_left)

        # Maintain size property
        if len(self.small) < len(self.large):
            smallest_right = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_right)


    def findMedian(self) -> float:
        
        m = len(self.small)
        n = len(self.large)

        if m == n:
            median = (-self.small[0] + self.large[0]) / 2
        
        else:
            median = -self.small[0]
        
        return median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
