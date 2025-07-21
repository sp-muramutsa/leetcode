class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = self.bisect_left(self.store[key], timestamp)

        if idx > -1:
            return self.store[key][idx][1]
        return ""

    def bisect_left(self, arr: list, target: int) -> int:
        l, r = 0, len(arr)

        while l < r:

            mid = l + (r - l) // 2
            if arr[mid][0] <= target:
                l = mid + 1
            else:
                r = mid

        return l - 1


# key: [(timestamp, value)]
# Is timestamp <= target?
# Truth: T, T, T, T, T, F, F, F, F, ..
# If T
# we're left. l = mid. This might be the last truth
# Otherwise
# we're right. r = mid - 1.
# At the end, return r - 1.
# [1, 4] [T, T] target = 4  idx = 1
# [1, 4] [T, T] target = 5 idx = 1
# [10, 20] target = 5. [F, F]
# [10, 20] target = 10. [T, F]
# [10, 20] target = 15. [T, F]
# [10, 20] target = 20. [T, T]
# [10, 20] target = 25. [T, T]
# Is timestamp > target?
# T, T, T, T, F -> We want to return the last True if any.

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

