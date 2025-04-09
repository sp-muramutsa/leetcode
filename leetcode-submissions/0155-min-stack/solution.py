class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if self.stack:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
