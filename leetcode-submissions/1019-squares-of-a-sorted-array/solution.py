class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two pointer approach
        Time: O(n)
        Space: O(n)
        Intuition: Use two pointers. Comparing the two values at the extremes and determining which one will fill in a certain position.
        """

        length = len(nums)
        result = [0] * length

        l, r = 0, length - 1
        i = r

        while i >= 0:
            l_square = nums[l] ** 2
            r_square = nums[r] ** 2

            if l_square > r_square:
                result[i] = l_square
                l += 1
            else:
                result[i] = r_square
                r -= 1

            i -= 1
        return result
 
