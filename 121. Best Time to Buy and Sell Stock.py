class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_buy = float("inf")
        best_profit = 0

        # rank sell times in order of preference
        sell_times = iter(reversed(sorted(
            list(range(0, len(prices))),
            key=lambda i: prices[i]
        )))

        buy = 0
        sell = next(sell_times)

        while buy < len(prices):
            if sell < buy:
                try:
                    sell = next(sell_times)
                except StopIteration:
                    break
            elif prices[buy] >= lowest_buy:
                buy += 1
            else:
                profit = prices[sell] - prices[buy]
                best_profit = max(best_profit, profit)
                lowest_buy = min(lowest_buy, prices[buy])

                buy += 1
        
        return best_profit
