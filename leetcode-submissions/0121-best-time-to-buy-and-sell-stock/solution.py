class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Keep track of the smallest purchase price. The maximum profit has of course the minimum purchase. So use each index to update the max profit.
        """
        l, r = 0, 1
        n = len(prices)
        max_profit = 0
        smallest = prices[l]

        while r < n:
            if prices[r] <= smallest:
                smallest = prices[r]
            max_profit = max(max_profit, prices[r] - smallest)
            r += 1
        
        return max_profit
        
