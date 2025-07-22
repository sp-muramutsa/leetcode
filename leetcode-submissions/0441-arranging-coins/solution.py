class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        
        # k * (k + 1)) // 2 <= n
        # k ** 2 + k <= 2n
        # 2n >= k ** 2 + k
        # 2n >= (k + 0.5) ** 2 - 0.25
        # 2n + 0.25 >= (k + 0.5) ** 2
        # sqrt(2n + 0.25) - 0.5 >= k
        # 

        k = sqrt(2 * n + 0.25) - 0.5
        return floor(k)
        
        
