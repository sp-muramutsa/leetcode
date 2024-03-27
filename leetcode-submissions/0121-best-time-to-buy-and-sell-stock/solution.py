class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        Intuition: use two pointers(sliding window) iteration form left to right to compare possible profits and find a maximum
        Time: O(n)
        Space: O(1)
        """

        number_of_days = len(prices)
        buy, sell = 0, 1
        maximum_profit = 0

        while sell < number_of_days:
            profit = prices[sell] - prices[buy]
            if profit > 0:
                if profit > maximum_profit:
                    maximum_profit = profit
                sell += 1
            else:
                buy = sell
                sell += 1
                
        return maximum_profit

                
          


        
