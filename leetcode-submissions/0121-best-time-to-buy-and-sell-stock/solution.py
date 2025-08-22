class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Choose the day woth lowest cost
        # Create a profit variable
        # Create 2 pointers 
        # while r is less than the length 
        # Find the difference
        # Update the profit
        profit = 0
        l, r = 0, 1
        while r <= len(prices) - 1:
            diff = prices[r] - prices[l]
            profit = max(profit, diff)
            
            if prices[l] > prices[r]:
                l = r
                
            r += 1
            
        return profit
