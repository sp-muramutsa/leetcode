class Solution:
    def fib(self, n: int) -> int:

        if n == 0 or n == 1:
            return n

        prev_2, prev_1 = 0, 1

        for i in range(2, n):
            curr = prev_1 + prev_2
            prev_1, prev_2 = curr, prev_1

        return prev_1 + prev_2

