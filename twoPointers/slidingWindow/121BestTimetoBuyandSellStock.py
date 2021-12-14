from typing import List


def maxProfit(self, prices: List[int]) -> int:
        left = 0
        n = len(prices)
        maxP = 0
        for right in range(1, n):
            # profitable?
            
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
                
            else:
                left = right
                
        return maxP
        