class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Time: O(logn)
        Space: O(1)
        Intuition: Take advantage of the numbers sorted quality and utilize binary search to halve the search space. Remember to return a rounded down.
        """
        lo, hi = 0, x

        while lo <= hi:
            mid = lo + (hi - lo) // 2
              
            if mid * mid > x:
                hi = mid - 1
            elif mid * mid == x:
                return mid
            else:
                lo = mid + 1
        return lo - 1

