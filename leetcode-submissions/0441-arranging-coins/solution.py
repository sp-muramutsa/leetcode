class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Quadratic Solution
        Time: O(1)
        Space: O(1)
        Intuition: Follows the previous approach. But goes further. Solve the quadratic equation is r * ( r + 1) // 2 = n. r is the solution. Round down!!!!!!
        This solution makes sense from a mathematical perspective but from a programming one it might be a stretch. The binary search one is recommended!
        """
        
        # Quadratic Solution
        # r * (r + 1) = 2n
        # r** 2 + r - 2n = 0

        delta = 1 + (8 * n)

        r1 = (1 + sqrt(delta)) / 2
        r2 = (1 - sqrt(delta)) / 2
        return floor(abs(r2))

       

