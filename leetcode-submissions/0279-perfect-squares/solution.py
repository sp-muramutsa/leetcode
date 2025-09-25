class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        cache = {}

        def dfs(rem):
            if rem == 0:
                return 0
            if rem in cache:
                return cache[rem]

            res = float("inf")
            for i in squares:
                if i <= rem:
                    res = min(res, 1 + dfs(rem - i))

            cache[rem] = res

            return res

        return dfs(n)
