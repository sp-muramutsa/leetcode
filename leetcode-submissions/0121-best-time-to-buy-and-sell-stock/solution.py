class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1

        n = len(prices)
        max_profit = 0

        while r < n:
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r
            
            r += 1
        
        return max_profit


            
