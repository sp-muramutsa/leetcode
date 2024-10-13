# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        Intuition: Binary search. https://www.youtube.com/watch?v=tgVSkMA8joQ&t=426s&ab_channel=mCoding
        """
        lo, hi = 0, n

        while lo < hi:
            mid = lo + (hi-lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
                
        
        return lo

        
