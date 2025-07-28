class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        n = len(self.store[key])
        l, r = 0, n

        while l < r:
            mid = l + (r - l) // 2

            if self.store[key][mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid

        idx = l - 1
        if 0 <= idx < n:
            return self.store[key][idx][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

