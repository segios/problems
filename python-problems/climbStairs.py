# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs
# Easy
# Dynamic Programming
# C 
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/

from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [None] * (n+1)
        DP[0] = 0
        DP[1] = 1
      
        if n > 1:
            DP[2] = 2

        for i in range(3, n+1):
            DP[i] = DP[i-1] + DP[i-2]

        return DP[n]



solution = Solution()

res = solution.climbStairs(1)
print (res)

res = solution.climbStairs(2)
print (res)

res = solution.climbStairs(3)
print (res)

res = solution.climbStairs(4)
print (res)