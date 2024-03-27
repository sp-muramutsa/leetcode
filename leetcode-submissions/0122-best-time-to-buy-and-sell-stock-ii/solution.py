class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        number_of_days = len(prices)
        profit = 0

        for i in range(1, number_of_days):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1] # Sell
        
        return profit


        
