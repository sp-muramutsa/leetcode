class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        # 3
        a, b, c = 0, 1, 1

        for i in range(3, n + 1):
            temp = a + b + c
            a = b
            b = c
            c = temp

        return temp

