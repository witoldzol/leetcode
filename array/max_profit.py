from typing import List

input = [7,1,5,3,6,4]
expected = 7
# 1,3,4,5,6,7


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current = None
        for i,p in enumerate(prices):
            if current is None:
                if (i +1) < len(prices) and prices[i+1] > p:
                    # buy
                    current = p
                    profit -= p
            else:
                if (i +1) < len(prices) and prices[i+1] > p:
                    continue
                    # don't sell, wait for tomorrow
                else:
                    if p > current:
                        # sell now
                        profit += p
                        current = None
        if current:
            profit += current
        print(f"{profit=}")
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current = prices[0]
        for p in prices:
            if current < p:
                profit += (p - current)
            current = p
        return profit



assert expected == Solution().maxProfit(input)
