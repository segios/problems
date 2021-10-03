# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock
# Easy
# Dynamic Programming
# A
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/
import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) == 1 :
            return 0

        buyIdx, sellIdx = 0, 1
        maxProfit = prices[sellIdx] - prices[buyIdx]

        for p in range(1, len(prices)):
            if prices[p] < prices[buyIdx] and p < len(prices)-1:
                buyIdx = p
                if sellIdx <= p:
                    sellIdx = p + 1
            
            if prices[p] > prices[sellIdx]:
                sellIdx = p

            if maxProfit < prices[sellIdx] - prices[buyIdx]:
                maxProfit = prices[sellIdx] - prices[buyIdx]


        if (maxProfit < 0):
            maxProfit = 0

        return maxProfit


class SolutionDemo:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = sys.maxsize
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit

solution = Solution()

res = solution.maxProfit([1,2,4])
print (res)

res = solution.maxProfit([7,1,5,3,6,4])
print (res)

res = solution.maxProfit([5,5,4,9,3,8,5,5,1,6,8,3,4])
print (res)

res = solution.maxProfit([7,6,4,3,1])
print (res)

res = solution.maxProfit([2,4,1])
print (res)


res = solution.maxProfit([7,1,5,3,6,4])
print (res)

