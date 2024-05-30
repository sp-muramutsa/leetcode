class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Binary search
        Time: O(logn)
        Space: O(1)
        Intuition: Use binary search to halve the search space.
        """

        lo, hi = 0, num

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False


