class Solution:
    def gaussian_sum(self, k) -> int:
        return (k * (k + 1)) // 2

    def arrangeCoins(self, n: int) -> int:

        if n == 1:
            return n

        l, r = 1, n

        while l < r:
            mid = l + (r - l) // 2
            if self.gaussian_sum(mid) <= n:
                l = mid + 1
            else:
                r = mid

        return l - 1

