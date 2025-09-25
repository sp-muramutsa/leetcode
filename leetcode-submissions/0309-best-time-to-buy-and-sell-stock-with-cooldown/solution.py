class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = True
        n = len(prices)

        @lru_cache
        def f(i, indicator):

            if i >= n:
                return 0

            # Cooldown
            max_profit = f(i + 1, indicator)

            # Buy
            if indicator:
                buy = f(i + 1, False) - prices[i]
                max_profit = max(max_profit, buy)

            # Sell
            else:
                sell = f(i + 2, True) + prices[i]
                max_profit = max(max_profit, sell)

            return max_profit

        return f(0, True)

