class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            idx = self.bisect_right(self.map[key], timestamp)
            self.map[key].insert(idx, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        idx = self.bisect_right(self.map[key], timestamp) - 1

        return self.map[key][idx][1] if idx >= 0 else ""
    
    def bisect_right(self, arr, target):
        l, r = 0, len(arr) 

        while l < r:
            mid = (l+r) // 2
            if arr[mid][0] <= target:
                l = mid + 1
            else:
                r = mid 
        
        return l 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

