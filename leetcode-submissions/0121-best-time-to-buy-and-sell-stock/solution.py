class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l, r = 0, 1
        n = len(prices)

        while r < n:
            # profit can be made
            if prices[r] - prices[l] > 0:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1

            # profit can't be made
            else:
                l = r
                r += 1
            
        
        return max_profit
