# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock
# Easy
# Dynamic Programming
# B 
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/
import sys
from typing import List

class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        minIndex = 0
        maxIndex = -1
        solution = None

        if(len(prices) == 0):
            return 0

        for i in range(1, len(prices)):
            if maxIndex == -1 and prices[i] > prices[minIndex]:
                maxIndex = i
            elif maxIndex != -1 and prices[maxIndex] < prices[i] :
                maxIndex = i
            
            elif prices[i] < prices[minIndex]:
                if  i < maxIndex or maxIndex == -1: 
                    minIndex = i
                else:
                    if solution == None:
                        solution = (minIndex, maxIndex)
                        maxIndex = -1
                        minIndex = i
                    else:
                        if prices[solution[1]] < prices[maxIndex]:
                            solution = (solution[0], maxIndex)
                        
                        if prices[solution[1]] - prices[solution[0]] < prices[maxIndex] - prices[minIndex] :
                            solution = (minIndex, maxIndex)
                            maxIndex = -1
                            minIndex = i
                        else:
                            maxIndex = -1
                            minIndex = i


        if(maxIndex != -1) and solution != None:
            if prices[solution[1]] < prices[maxIndex]:
                solution = (minIndex, maxIndex)   
        
        if solution != None and maxIndex != -1:
            return max(prices[maxIndex] - prices[minIndex],prices[solution[1]]-prices[solution[0]]) 
        elif solution != None:
            return prices[solution[1]]-prices[solution[0]]
        elif maxIndex != -1:
            return prices[maxIndex] - prices[minIndex]
        else:
            return 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = sys.maxsize
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit


# public class Solution {
#     public int maxProfit(int prices[]) {
#         int minprice = Integer.MAX_VALUE;
#         int maxprofit = 0;
#         for (int i = 0; i < prices.length; i++) {
#             if (prices[i] < minprice)
#                 minprice = prices[i];
#             else if (prices[i] - minprice > maxprofit)
#                 maxprofit = prices[i] - minprice;
#         }
#         return maxprofit;
#     }
# }

class Solution_Brute:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if max < prices[j] - prices[i]:
                    max = prices[j] - prices[i]
        return max

solution = Solution()

res = solution.maxProfit([5,5,4,9,3,8,5,5,1,6,8,3,4])
print (res)

res = solution.maxProfit([7,6,4,3,1])
print (res)

res = solution.maxProfit([2,4,1])
print (res)


res = solution.maxProfit([7,1,5,3,6,4])
print (res)

