class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 0, num

        while l <= r:
            mid = l + (r - l) // 2

            if mid**2 > num:
                r = mid - 1

            elif mid**2 < num:
                l = mid + 1

            else:
                return True

        return False

