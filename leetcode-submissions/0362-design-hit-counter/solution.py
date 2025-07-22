class HitCounter:

    def __init__(self):
        self.hits = deque([])

    def hit(self, timestamp: int) -> None:
        self.hits.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        print(self.hits, timestamp)
        # i = len(self.hits) - 1
        # count = 0

        # while i >= 0:
        #     if timestamp - self.hits[i] < 300:
        #         count += 1
        #     else:
        #         return count
        #     i -= 1
        
        # return count
        n = len(self.hits)
        l, r = 0, n

        while l < r:
            mid = l + (r - l) // 2

            # Left
            if timestamp - self.hits[mid] < 300:
                l = mid + 1
            else:
                r = mid
        

        return l

            
        # Is timestamp - nums[mid] < 300?
        # Return the first False.
        # [1, 2, 3], 4
        # [T, T, T] 
        # [1, 2, 3, 300], 300, return 4
        #
        # 1, 2, 3, 300], 301, 
        # 

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

