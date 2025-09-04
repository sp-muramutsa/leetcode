class Solution:
    def fib(self, n: int) -> int:
        # Tabulation with optimized space complexity O(1)
        # The time complexity is still O(n)
        # We use prev and curr pointer to keep track of the current position 
        # Return the curr position

        if n <= 1:
            return n

        prev, curr = 0, 1

        for i in range(2, n+1):
            tmp = prev + curr

            prev = curr
            curr = tmp
        return curr
