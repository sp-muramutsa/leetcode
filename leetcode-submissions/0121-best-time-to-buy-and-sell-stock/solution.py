class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0
        for i in range(len(prices)-1):
            diff = prices[right] - prices[left]
            if diff < 0:
                left = right 
            
            right += 1
            profit = max(profit, diff)
        return profit

