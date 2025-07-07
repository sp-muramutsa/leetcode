from collections import defaultdict, Counter


class FreqStack:
    def __init__(self):
        self.counter = Counter()  # val -> freq
        self.groups = defaultdict(list)  # freq -> [list of vals]
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        frequency = self.counter[val]
        self.groups[frequency].append(val)
        self.max_freq = max(self.max_freq, frequency)

    def pop(self) -> int:
        max_frequency = self.max_freq

        # Get the top element among those with max_frequency
        val = self.groups[self.max_freq].pop()
        self.counter[val] -= 1

        # Check if there is any element left with max_freq. If not, then reduce max_freq
        if not self.groups[self.max_freq]:
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

