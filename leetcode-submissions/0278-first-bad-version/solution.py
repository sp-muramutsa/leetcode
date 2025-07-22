# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:

        # [G, G, G, B, B]
        # We want to return the first Bad version
        # Bisect left

        l, r = 0, n

        while l < r:
            mid = l + (r - l) // 2

            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid

        return l

