from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = SortedDict({timestamp: value})
        else:
            self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        idx = self.map[key].bisect_right(timestamp)

        return self.map[key].peekitem(idx - 1)[1] if idx > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

