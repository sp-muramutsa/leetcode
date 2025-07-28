class HitCounter:

    def __init__(self):
        self.counter = []

    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        n = len(self.counter)
        l, r = 0, n

        while l < r:
            mid = l + (r - l) // 2
            if timestamp - self.counter[mid] >= 300:
                l = mid + 1
            else:
                r = mid

        return len(self.counter[l:n])


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

