class Solution:
    def fib(self, n: int) -> int:
        # Create a list that keeps the calculation of numbers
        dp = [-1] * (n+1)
        # Base case if the number index is not -1 return the number
        def dfs(num):
            if num == 1:
                return 1
            if num == 0:
                return 0
            
            if dp[num] != -1:
                return dp[num]
            
            dp[num] = (dfs(num-1) + dfs(num-2))
            return dp[num]
        # Return the sum of recursively called num -1 and num - 2
        return dfs(n)
        
